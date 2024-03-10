#!/usr/bin/python3
"""an storage engine implementation"""
from os import path
import json


class FileStorage:
    """serialize instances to and from JSON file and deserialize
    JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

    def clear_objects(self):
        """clears __obj for retaining a clean dict"""
        FileStorage.__objects.clear()

    def path(self):
        """return file_path"""
        return FileStorage.__file_path

    def all(self):
        """return __object dict"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __object the obj with key
        possessing syntax <obj classname>.id

        Args:
            obj (obj) - python BaseModel object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file(__file_path)
        """
        ser_objects = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(ser_objects))

    def reload(self):
        """
        deserializes JSON file(__file_path) to __objects only if JSON
        file exist, otherwise, do nothing
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                # check if file is empty
                contents = f.read()
                if contents:
                    des_objects = json.loads(contents)
                    FileStorage.__objects = {k: self.create_object(v)
                                      for k, v in des_objects.items()
                                      }
                else:
                    return

    def create_object(self, object_dict):
        """
        This method is used to create an object
        of the class based on the dictionary
        """
        from models.base_model import BaseModel
        class_name = object_dict['__class__']
        if class_name == 'User':
            from models.user import User
            return User(**object_dict)
        elif class_name == 'State':
            from models.state import State
            return State(**object_dict)
        elif class_name == 'City':
            from models.city import City
            return City(**object_dict)
        elif class_name == 'Amenity':
            from models.amenity import Amenity
            return Amenity(**object_dict)
        elif class_name == 'Review':
            from models.review import Review
            return Review(**object_dict)
        elif class_name == 'Place':
            from models.place import Place
            return Place(**object_dict)
        else:
            return BaseModel(**object_dict)
