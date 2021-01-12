from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
import datetime

from db.db_connection import Base, engine


class BillInDB(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_bill = Column(DateTime, default=datetime.datetime.utcnow)
    seller = Column(String, ForeignKey("employees.id_employee"))
    client = Column(String, ForeignKey("clients.id_client"))
    total_value = Column(Float)


Base.metadata.create_all(bind=engine)
