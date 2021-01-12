from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
import datetime

from db.db_connection import Base, engine


class DetailInDB(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bill_number = Column(Integer, ForeignKey("bills.id"))
    code_product_details = Column(String, ForeignKey("products.code_product"))
    quantity_product = Column(Integer)
    total_value_product = Column(Float)


Base.metadata.create_all(bind=engine)
