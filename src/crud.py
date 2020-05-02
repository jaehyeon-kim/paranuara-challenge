from typing import List, Any
from sqlalchemy import func
from sqlalchemy.orm import Session
from src import models, schemas

FOOD_GROUPS = {
    "fruits": ["apple", "banana", "orange", "strawberry"],
    "vegetables": ["beetroot", "carrot", "celery", "cucumber"],
}


def get_intersection(first_list: List[Any], second_list: List[Any]):
    return list(set(first_list).intersection(set(second_list)))


def group_food(food: List[str]):
    return {
        "fruits": get_intersection(FOOD_GROUPS["fruits"], food),
        "vegetables": get_intersection(FOOD_GROUPS["vegetables"], food),
    }


def get_num_companies(db: Session):
    return db.query(func.count(models.Company.id)).first()[0]


def get_companies(db: Session, skip: int = 0, limit: int = 50):
    companies_info = (
        db.query(models.Company.id, models.Company.name).offset(skip).limit(limit).all()
    )
    return {
        "companies": [{"id": info[0], "name": info[1]} for info in companies_info],
        "skip": skip,
        "limit": limit,
        "total": get_num_companies(db),
    }


def get_company_employees(db: Session, company_id: int):
    company = db.query(models.Company).filter(models.Company.id == company_id).first()
    return company.employees if company else None


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_filtered_friends(
    db: Session, friend_ids: List[int], eye_colour: str = "brown", has_died: bool = False
):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id.in_(friend_ids))
        .filter(models.Employee.eye_colour == eye_colour)
        .filter(models.Employee.has_died == has_died)
        .all()
    )


def get_employee_relation(db: Session, first_id: int, second_id: int):
    first_employee = get_employee(db, first_id)
    second_employee = get_employee(db, second_id)
    if any([not first_employee, not second_employee]):
        return None
    else:
        friend_ids = get_intersection(
            [e.friend_id for e in first_employee.friends],
            [e.friend_id for e in second_employee.friends],
        )
        return {
            "first_employee": first_employee,
            "second_employee": second_employee,
            "friends": get_filtered_friends(db, friend_ids),
        }


def get_employee_food(db: Session, employee_id: int):
    employee = get_employee(db, employee_id)
    return (
        {
            **{"username": employee.name, "age": employee.age},
            **group_food([f.name for f in employee.favourite_food]),
        }
        if employee
        else None
    )
