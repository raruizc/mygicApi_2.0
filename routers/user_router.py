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


@router.post("/user/auth/")
async def auth_user(user_in: UserIn, db: Session = Depends(get_db)):
    user_in_db = db.query(UserInDB).get(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return {"Autenticado": True}
