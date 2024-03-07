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

    def all(self):
        """return __object dict"""
        return __objects

    def new(self, obj):
        """sets in __object the obj with key
        possessing syntax <obj classname>.id

        Args:
            obj (obj) - python baseModel object
        """
        key = f"{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file(__file_path)
        """
        if self.__objects:
            with open(self.__file_path, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(self.__objects))

    def reload(self):
        """
        deserializes JSON file(__file_path) to __objects only if JSON
        file exist, otherwise, do nothing
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                self.__objects = json.loads(f.read())
