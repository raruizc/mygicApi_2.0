from sqlalchemy import Column, Integer, String, Float

from db.db_connection import Base, engine


class EmployeeInDB(Base):
    __tablename__ = "employees"

    id_employee = Column(String, primary_key=True, unique=True)
    type_document = Column(String)
    name_employee = Column(String)
    surname_employee = Column(String)
    address_employee = Column(String)
    phone_employee = Column(String)
    email_employee = Column(String)
    charge_employee = Column(String)
    salary = Column(Float)


Base.metadata.create_all(bind=engine)
