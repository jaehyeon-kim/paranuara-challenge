from typing import List
from pydantic import BaseModel


class EmployeeFeature(BaseModel):
    id: int
    employee_id: int


class FavouriteFood(EmployeeFeature):
    name: str

    class Config:
        orm_mode = True


class Friends(EmployeeFeature):
    friend_id: int

    class Config:
        orm_mode = True


class IdNamePair(BaseModel):
    id: int
    name: str


class Employee(IdNamePair):
    age: int
    address: str
    phone: str
    eye_colour: str
    has_died: bool
    company_id: int
    favouriteFood: List[FavouriteFood] = []
    friends: List[Friends] = []

    class Config:
        orm_mode = True


class Company(IdNamePair):
    employees: List[Employee] = []

    class Config:
        orm_mode = True
