from sqlalchemy import Column, Integer, String, Float

from db.db_connection import Base, engine


class ProductInDB(Base):
    __tablename__ = "products"

    code_product = Column(String, primary_key=True, unique=True)
    name_product = Column(String)
    reference_product = Column(String)
    description_product = Column(String)
    quantity_available = Column(Integer)
    price_producto = Column(Float)


Base.metadata.create_all(bind=engine)
