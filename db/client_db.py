from sqlalchemy import Column, Integer, String, Float, Date

from db.db_connection import Base, engine


class ClientInDB(Base):
    __tablename__ = "clients"

    id_client = Column(String, primary_key=True, unique=True)
    type_document = Column(String)
    name_client = Column(String)
    surname_client = Column(String)
    address_client = Column(String)
    phone_client = Column(String)
    email_client = Column(String)


Base.metadata.create_all(bind=engine)
