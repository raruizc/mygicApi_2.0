from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgres://bqdcastqoomved:9135179f10126c649dc7eecf5e34e93673561e18c14059d0eb673050ee5a2c80@ec2-54-157-12-250.compute-1.amazonaws.com:5432/ddljag3i0mscp1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
Base.metadata.schema = "mygic"
