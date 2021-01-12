from pydantic import BaseModel


class ClientIn(BaseModel):
    id_client: str
    type_document: str
    name_client: str
    surname_client: str
    address_client: str
    phone_client: str
    email_client: str


class ClientOut(BaseModel):
    id_client: str
    type_document: str
    name_client: str
    surname_client: str
    address_client: str
    phone_client: str
    email_client: str

    class Config:
        orm_mode = True
