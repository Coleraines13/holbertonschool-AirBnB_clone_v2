#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from models.user import User


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id',
            ForeignKey('places.id'),
            nullable=False,
            primary_key=True),
        Column('amenity_id',
            ForeignKey('amenities.id'),
            nullable=False,
            primary_key=True)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                            cascade="all, delete, delete-orphan",
                            backref='place')
        amenities = relationship('Amenity',
                        secondary="place_amenity",
                        viewonly=False,
                        backref="place_amenities"
                )

    else:
        @property
        def user(self):
            """this will get the owner of the place"""
            from models import storage
            return storage.all(User).get("User.{}".format(self.user_id))

        @property
        def amenities(self):
            """this returns amenities of place"""
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]


        @amenities.setter
        def amenities(self, obj):
            """this adds an amenity to place"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """Returns the reviews of this Place"""
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]
