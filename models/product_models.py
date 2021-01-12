from pydantic import BaseModel


class ProductIn(BaseModel):
    code_product: str
    name_product: str
    reference_product: str
    description_product: str
    quantity_available: int
    price_producto: float


class ProductOut(BaseModel):
    code_product: str
    name_product: str
    reference_product: str
    description_product: str
    quantity_available: int
    price_producto: float

    class Config:
        orm_mode = True
