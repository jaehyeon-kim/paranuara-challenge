from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import models, schemas
from src.database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_companies(db: Session):
    return db.query(models.Company).filter(models.Company.id == 26).first()


@app.get("/companies/", response_model=schemas.Company)
def get_company(db: Session = Depends(get_db)):
    db_users = get_companies(db)
    return db_users


# from sqlalchemy.orm import Session
# from src import models, schemas, database


# def get_companies(db: Session):
#     return db.query(models.Company).first()


# get_companies(database.SessionLocal())

# from src.database import SessionLocal
# from src.models import Employee, Company
# from sqlalchemy.orm import sessionmaker

# session = SessionLocal()

# e = session.query(Employee).first()
# c = session.query(Company).first()

# c.id

# for instance in session.query(Company).first():
#     print(instance.employees)
