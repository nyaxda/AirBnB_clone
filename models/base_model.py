#!/usr/bin/python3
"""Defines a base class for all models in this project"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
