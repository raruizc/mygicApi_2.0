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


@router.post("/employee/", response_model=EmployeeOut)
async def create_employee(employee_in: EmployeeIn, db: Session = Depends(get_db)):
    employee_in_db = db.query(EmployeeInDB).get(employee_in.id_employee)

    if employee_in_db != None:
        raise HTTPException(status_code=400, detail="El empleado ya existe")

    employee_in_db = EmployeeInDB(**employee_in.dict())

    db.add(employee_in_db)
    db.commit()
    db.refresh(employee_in_db)

    return employee_in_db


@router.get("/employee/", response_model=List[EmployeeOut])
async def get_all_employees(db: Session = Depends(get_db)):
    employees_in_db = db.query(EmployeeInDB).all()
    return employees_in_db


@router.get("/employee/{id_employee}", response_model=EmployeeOut)
async def get_by_id(id_employee: str, db: Session = Depends(get_db)):
    employee_in_db = db.query(EmployeeInDB).get(id_employee)

    if employee_in_db == None:
        raise HTTPException(status_code=400, detail="El empleado no existe")

    return employee_in_db


@router.delete("/employee/{id_employee}", response_model=EmployeeOut)
async def delete_employee(id_employee: str, db: Session = Depends(get_db)):
    employee_in_db = db.query(EmployeeInDB).get(id_employee)

    if employee_in_db == None:
        raise HTTPException(status_code=400, detail="El empleado no existe")

    db.delete(employee_in_db)
    db.commit()

    return employee_in_db


@router.put("/employee/", response_model=EmployeeOut)
async def update_employee(employee_in: EmployeeIn, db: Session = Depends(get_db)):
    employee_in_db = db.query(EmployeeInDB).get(employee_in.id_employee)

    if employee_in_db == None:
        raise HTTPException(status_code=400, detail="El empleado no existe")

    db.query(EmployeeInDB).filter(EmployeeInDB.id_employee == employee_in.id_employee).update({EmployeeInDB.type_document: employee_in.type_document,
                                                                                               EmployeeInDB.name_employee: employee_in.name_employee,
                                                                                               EmployeeInDB.surname_employee: employee_in.surname_employee,
                                                                                               EmployeeInDB.address_employee: employee_in.address_employee,
                                                                                               EmployeeInDB.phone_employee: employee_in.phone_employee,
                                                                                               EmployeeInDB.email_employee: employee_in.email_employee,
                                                                                               EmployeeInDB.charge_employee: employee_in.charge_employee,
                                                                                               EmployeeInDB.salary: employee_in.salary
                                                                                               })
    db.commit()

    return employee_in
