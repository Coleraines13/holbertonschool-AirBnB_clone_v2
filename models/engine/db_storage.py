#!/usr/bin/python3
"""this will define a class to manage data base storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

mapped_classes = (City, State, User, Place, Amenity, Review)


class DBStorage:
    """this class stores models"""
    __engine = None
    __session = None

    def __init__(self):
        """initializer"""
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                usr, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """this returns a dictionary of models"""
        objs = {}
        if cls in mapped_classes:
            objs.update({"{}.{}".format(cls.__name__, item.id): item
                for item in self.__session.query(cls)})
        elif cls is None:
            for c in mapped_classes:
                objs.update({"{}.{}".format(c.__name__, item.id): item
                    for item in self.__session.query(c)})
            return objs

    def delete(self, obj=None):
        """this removes an object from database"""
        if obj in self.all(type(obj).values()):
            self.__session.delete(obj)

    def new(self, obj):
        """this adds a new object to databse"""
        if type(obj) in mapped_classes:
            self.__session.add(obj)

    def save(self):
        """this commits anychanges made to database"""
        self.__session.commit()

    def reload(self):
        """this loads the storage from database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                    expire_on_commit=False))

    def close(self):
        """this closes the sotrage engine"""
        self.__session.remove()
