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


@router.post("/client/", response_model=ClientOut)
async def create_client(client_in: ClientIn, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(client_in.id_client)

    if client_in_db != None:
        raise HTTPException(status_code=400, detail="El cliente ya existe")

    client_in_db = ClientInDB(**client_in.dict())

    db.add(client_in_db)
    db.commit()
    db.refresh(client_in_db)

    return client_in_db


@router.get("/client/", response_model=List[ClientOut])
async def get_all_clients(db: Session = Depends(get_db)):
    clients_in_db = db.query(ClientInDB).all()
    return clients_in_db


@router.get("/client/{id_client}", response_model=ClientOut)
async def get_by_id(id_client: str, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(id_client)

    if client_in_db == None:
        raise HTTPException(status_code=400, detail="El cliente no existe")

    return client_in_db


@router.delete("/client/{id_client}", response_model=ClientOut)
async def delete_client(id_client: str, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(id_client)

    if client_in_db == None:
        raise HTTPException(status_code=400, detail="El cliente no existe")

    db.delete(client_in_db)
    db.commit()

    return client_in_db


@router.put("/client/", response_model=ClientOut)
async def update_client(client_in: ClientIn, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(client_in.id_client)

    if client_in_db == None:
        raise HTTPException(status_code=400, detail="El cliente no existe")

    db.query(ClientInDB).filter(ClientInDB.id_client == client_in.id_client).update({ClientInDB.type_document: client_in.type_document,
                                                                                     ClientInDB.name_client: client_in.name_client,
                                                                                     ClientInDB.surname_client: client_in.surname_client,
                                                                                     ClientInDB.address_client: client_in.address_client,
                                                                                     ClientInDB.phone_client: client_in.phone_client,
                                                                                     ClientInDB.email_client: client_in.email_client
                                                                                     })
    db.commit()

    return client_in
