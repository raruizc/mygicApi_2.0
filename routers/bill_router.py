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


@router.post("/bill/", response_model=BillOut)
async def create_bill(bill_in: BillIn, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(bill_in.client)
    employee_in_db = db.query(EmployeeInDB).get(bill_in.seller)

    if client_in_db == None:
        raise HTTPException(status_code=400, detail="El cliente no existe")

    if employee_in_db == None:
        raise HTTPException(status_code=400, detail="El empleado no existe")

    bill_in_db = BillInDB(**bill_in.dict(), total_value=0)

    db.add(bill_in_db)
    db.commit()
    db.refresh(bill_in_db)

    return bill_in_db


@router.get("/bill/", response_model=List[BillOut])
async def get_all_bills(db: Session = Depends(get_db)):
    bills_in_db = db.query(BillInDB).all()
    return bills_in_db


@router.get("/bill/{id}", response_model=BillOut)
async def get_by_id(id: int, db: Session = Depends(get_db)):
    bill_in_db = db.query(BillInDB).get(id)

    if bill_in_db == None:
        raise HTTPException(status_code=400, detail="La factura no existe")

    return bill_in_db


@router.delete("/bill/{id}", response_model=BillOut)
async def delete_bill(id: int, db: Session = Depends(get_db)):
    bill_in_db = db.query(BillInDB).get(id)

    if bill_in_db == None:
        raise HTTPException(status_code=400, detail="La factura no existe")

    db.delete(bill_in_db)
    db.commit()

    return bill_in_db
