from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    age = Column(Integer)
    address = Column(String)
    phone = Column(String)
    eye_colour = Column(String)
    has_died = Column(Boolean)
    company_id = Column(Integer, ForeignKey("companies.id"))

    favourite_food = relationship("FavouriteFood", backref="favourite_food_ref")
    friends = relationship("Friend", backref="friends_ref")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    employees = relationship("Employee", backref="employees_ref")


class FavouriteFood(Base):
    __tablename__ = "favourite_food"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    name = Column(String)


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    friend_id = Column(Integer)
