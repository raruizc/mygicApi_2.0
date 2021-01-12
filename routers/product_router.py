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


@router.post("/product/", response_model=ProductOut)
async def create_product(product_in: ProductIn, db: Session = Depends(get_db)):
    product_in_db = db.query(ProductInDB).get(product_in.code_product)

    if product_in_db != None:
        raise HTTPException(status_code=400, detail="El producto ya existe")

    product_in_db = ProductInDB(**product_in.dict())

    db.add(product_in_db)
    db.commit()
    db.refresh(product_in_db)

    return product_in_db


@router.get("/product/", response_model=List[ProductOut])
async def get_all_product(db: Session = Depends(get_db)):
    product_in_db = db.query(ProductInDB).all()
    return product_in_db


@router.get("/product/{code_product}", response_model=ProductOut)
async def get_by_code(code_product: str, db: Session = Depends(get_db)):
    product_in_db = db.query(ProductInDB).get(code_product)

    if product_in_db == None:
        raise HTTPException(status_code=400, detail="El producto no existe")

    return product_in_db


@router.delete("/product/{code_product}", response_model=ProductOut)
async def delete_product(code_product: str, db: Session = Depends(get_db)):
    product_in_db = db.query(ProductInDB).get(code_product)

    if product_in_db == None:
        raise HTTPException(status_code=400, detail="El producto no existe")

    db.delete(product_in_db)
    db.commit()

    return product_in_db


@router.put("/product/", response_model=ProductOut)
async def update_product(product_in: ProductIn, db: Session = Depends(get_db)):
    product_in_db = db.query(ProductInDB).get(product_in.code_product)

    if product_in_db == None:
        raise HTTPException(status_code=400, detail="El producto no existe")

    db.query(ProductInDB).filter(ProductInDB.code_product == product_in.code_product).update({ProductInDB.name_product: product_in.name_product,
                                                                                              ProductInDB.reference_product: product_in.reference_product,
                                                                                              ProductInDB.description_product: product_in.description_product,
                                                                                              ProductInDB.quantity_available: product_in.quantity_available,
                                                                                              ProductInDB.price_producto: product_in.price_producto
                                                                                              })
    db.commit()

    return product_in
