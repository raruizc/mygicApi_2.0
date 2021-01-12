from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db
from db.user_db import UserInDB
from db.client_db import ClientInDB
from db.employee_db import EmployeeInDB
from db.product_db import ProductInDB
from db.bill_db import BillInDB
from db.detail_bill_db import DetailInDB

from models.user_models import UserIn, UserOut
from models.client_models import ClientIn, ClientOut
from models.employee_models import EmployeeIn, EmployeeOut
from models.product_models import ProductIn, ProductOut
from models.bill_models import BillIn, BillOut
from models.detail_bill_models import DetailIn, DetailOut

router = APIRouter()


@router.put("/detail/", response_model=DetailOut)
async def select_product(detail_in: DetailIn, db: Session = Depends(get_db)):
    bill_in_db = db.query(BillInDB).get(detail_in.bill_number)
    product_in_db = db.query(ProductInDB).get(detail_in.code_product_details)

    if bill_in_db == None:
        raise HTTPException(status_code=400, detail="La factura no existe")

    if product_in_db == None:
        raise HTTPException(status_code=400, detail="El producto no existe")

    if product_in_db.quantity_available < detail_in.quantity_product:
        raise HTTPException(status_code=400,
                            detail="No se tiene la cantidad suficiente de " + product_in_db.name_product)

    subtotal = detail_in.quantity_product * product_in_db.price_producto

    bill_in_db.total_value = bill_in_db.total_value + subtotal
    db.commit()
    db.refresh(bill_in_db)

    product_in_db.quantity_available = product_in_db.quantity_available - \
        detail_in.quantity_product
    db.commit()
    db.refresh(product_in_db)

    detail_in_db = DetailInDB(**detail_in.dict(), total_value_product=subtotal)
    db.add(detail_in_db)
    db.commit()
    db.refresh(detail_in_db)

    return detail_in_db


@router.delete("/detail/{id}", response_model=DetailOut)
async def delete_detail(id: int, db: Session = Depends(get_db)):
    detail_in_db = db.query(DetailInDB).get(id)

    if detail_in_db == None:
        raise HTTPException(
            status_code=400, detail="El detalle en la factura no existe")

    bill_in_db = db.query(BillInDB).get(detail_in_db.bill_number)
    product_in_db = db.query(ProductInDB).get(
        detail_in_db.code_product_details)
    bill_in_db.total_value = bill_in_db.total_value - detail_in_db.total_value_product
    db.commit()
    db.refresh(bill_in_db)

    product_in_db.quantity_available = product_in_db.quantity_available + \
        detail_in_db.quantity_product
    db.commit()
    db.refresh(product_in_db)

    db.delete(detail_in_db)
    db.commit()

    return detail_in_db
