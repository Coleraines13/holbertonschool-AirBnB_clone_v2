#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, integer
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ this is the class of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
        cities = relationship('City',backref='state'
                             cascade='all, delete, delete-orphan',
    
    else:
        @property
        def cities(self):
            """this returns the cities in this State"""
            from models.city import City
            cities_in_state = []
            for obj in models.storage.all(City).values():
                if obj.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state 
