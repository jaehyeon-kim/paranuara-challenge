from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query, Path
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

app = FastAPI(title="Paranuara Challenge")

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get(
    "/company/list/",
    response_model=schemas.Company,
    tags=["company"],
    summary="Provide a list of companies - quick way to get company details",
)
def get_companies(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    db_users = crud.get_companies(db, skip, limit)
    return db_users


@app.get(
    "/company/{company_id}/employee",
    response_model=List[schemas.Employee],
    responses={404: {"model": schemas.BasicError}},
    tags=["company"],
    summary="Given a company, provide all the employees.",
)
def get_company_employees(
    company_id: int = Path(..., ge=0, description="non negative integer"),
    db: Session = Depends(get_db),
):
    employees = crud.get_company_employees(db, company_id)
    if employees is None:
        raise HTTPException(404, detail="company not found")
    if employees == []:
        raise HTTPException(404, detail="employees not found")
    return employees


@app.get(
    "/employee/relation/",
    response_model=schemas.EmployeeFriends,
    responses={404: {"model": schemas.BasicError}},
    tags=["employee"],
    summary="Given 2 people, provide their information and the list of their friends in common which have brown eyes and are still alive.",
)
def get_employee_relation(
    first_employee_id: int = Query(..., ge=0, description="non negative integer"),
    second_employee_id: int = Query(..., ge=0, description="non negative integer"),
    db: Session = Depends(get_db),
):
    employee_friends = crud.get_employee_relation(db, first_employee_id, second_employee_id)
    if not employee_friends:
        raise HTTPException(404, detail="one or more employees not found")
    return employee_friends


@app.get(
    "/employee/{employee_id}/favourite_food",
    response_model=schemas.EmployeeFood,
    responses={404: {"model": schemas.BasicError}},
    tags=["employee"],
    summary="Given 1 people, provide a list of fruits and vegetables they like.",
)
def get_employee_food(
    employee_id: int = Path(..., ge=0, description="non negative integer"),
    db: Session = Depends(get_db),
):
    employee_food = crud.get_employee_food(db, employee_id)
    print(employee_food)
    if not employee_food:
        raise HTTPException(404, detail="employee not found")
    return employee_food
