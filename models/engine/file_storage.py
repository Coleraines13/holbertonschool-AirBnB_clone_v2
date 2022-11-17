#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}


    def all(self, cls=None):
        """ this returns a dictionary of models"""
        if cls is None:
            return FileStorage.__objects
        else:
            new_obj = {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)}
            return (new_obj)

    def delete(self, obj=None):
        """this remives an object from the dictionary"""
        if obj is not None:
            return
        else:
            key - obj.__class__.__name__+ '.' + obj.id
            if key in self.all():
                del self.all()[key]
                self.save()

    def new(self, obj):
        """this adds a new object to the dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """this saves a storage dictionary"""
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """this loads a storage dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """this calls the reload method"""
        self.reload()
