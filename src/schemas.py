from typing import List
from pydantic import BaseModel


class IdName(BaseModel):
    id: int
    name: str


class Company(BaseModel):
    companies: List[IdName]
    start_id: int = 0
    limit: int = 50
    total: int


class FeatureBase(BaseModel):
    id: int
    employee_id: int


class FavouriteFood(FeatureBase):
    name: str

    class Config:
        orm_mode = True


class Friends(FeatureBase):
    friend_id: int

    class Config:
        orm_mode = True


class Employee(IdName):
    age: int
    address: str
    phone: str
    eye_colour: str
    has_died: bool
    company_id: int
    favourite_food: List[FavouriteFood] = []
    friends: List[Friends] = []

    class Config:
        orm_mode = True


class EmployeeFriends(BaseModel):
    first_employee: Employee
    second_employee: Employee
    friends: List[Employee]


class EmployeeFood(BaseModel):
    username: str
    age: int
    fruits: List[str]
    vegetables: List[str]


class BasicError(BaseModel):
    detail: str
