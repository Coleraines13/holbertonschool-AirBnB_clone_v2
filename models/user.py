#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """this defines the class user"""
    __tablename__ = 'users'
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    places = relationship('Place',
            cascade="all, delete, delete-orphan",
            backref='user')
    reviews = relationship('Review',
                            cascade="all, delete, delete-orphan",
                            backref='user')
