from pydantic import BaseModel


class EmployeeIn(BaseModel):
    id_employee: str
    type_document: str
    name_employee: str
    surname_employee: str
    address_employee: str
    phone_employee: str
    email_employee: str
    charge_employee: str
    salary: float


class EmployeeOut(BaseModel):
    id_employee: str
    type_document: str
    name_employee: str
    surname_employee: str
    address_employee: str
    phone_employee: str
    email_employee: str
    charge_employee: str
    salary: float

    class Config:
        orm_mode = True
