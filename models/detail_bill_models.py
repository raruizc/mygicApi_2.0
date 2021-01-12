from pydantic import BaseModel


class DetailIn(BaseModel):
    bill_number: int
    code_product_details: str
    quantity_product: int


class DetailOut(BaseModel):
    id: int
    bill_number: int
    code_product_details: str
    quantity_product: int
    total_value_product: float

    class Config:
        orm_mode = True
