from pydantic import BaseModel
from datetime import datetime


class BillIn(BaseModel):
    seller: str
    client: str


class BillOut(BaseModel):
    id: int
    date_bill: datetime
    seller: str
    client: str
    total_value: float

    class Config:
        orm_mode = True
