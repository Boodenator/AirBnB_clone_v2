#!/usr/bin/python3
"""User class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """new class for user
    Attributes:
        email: address of email
        password: login password
        first_name: 1st name
        last_name: lst name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
