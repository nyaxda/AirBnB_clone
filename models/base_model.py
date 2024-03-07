#!/usr/bin/python3
"""Defines a base class for all models in this project"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Represents the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel

        If kwargs is not empty, it will regenerate the instance
        else it will create a new instance

        Args:
            args (tuple) - positional arguements
            kwargs (list) - keyword/named arguements of an object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key in ("created_at", "updated_at"):
                    datetime_obj = datetime.fromisoformat(value)
                    self.__dict__[key] = datetime_obj
                    # setattr(self, key, datetime_obj)
                else:
                    self.__dict__[key] = value
                    # setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # call new() in storage engine to append the new instance
            self.storage.new()

    def __str__(self):
        """Returns a string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        `updated at` with the current datetime
        """
        self.updated_at = datetime.now()
        self.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        duplicate_dict = self.__dict__.copy()
        duplicate_dict["__class__"] = self.__class__.__name__
        duplicate_dict["created_at"] = self.created_at.isoformat()
        duplicate_dict["updated_at"] = self.updated_at.isoformat()
        return duplicate_dict
