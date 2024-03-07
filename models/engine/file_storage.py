#!/usr/bin/python3
"""an storage engine implementation"""
from os import path
import json


class FileStorage:
    """serialize instances to and from JSON file and deserialize
    JSON file to instances
    """
    __file_path = 'storage.json'
    __objects = {}
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

    def all(self):
        """return __object dict"""
        return self.__objects

    def new(self, obj):
        """sets in __object the obj with key
        possessing syntax <obj classname>.id

        Args:
            obj (obj) - python BaseModel object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file(__file_path)
        """
        if self.__objects:
            ser_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            with open(self.__file_path, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(ser_objects))

    def reload(self):
        """
        deserializes JSON file(__file_path) to __objects only if JSON
        file exist, otherwise, do nothing
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                des_objects = json.loads(f.read())
                self.__objects = {
                    k: self.create_object(v) for k, v in des_objects.items()}

    def create_object(self, object_dict):
        """
        This method is used to create an object
        of the class based on the dictionary
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        class_name = object_dict['__class__']
        if class_name == 'User':
            return User(**object_dict)
         elif class_name == 'State':
            return State(**object_dict)
        elif class_name == 'City':
            return City(**object_dict)
        elif class_name == 'Amenity':
            return Amenity(**object_dict)
        elif class_name == 'Review':
            return Review(**object_dict)
        elif class_name == 'Place':
            return Place(**object_dict)
        else:
            return BaseModel(**object_dict)
