#!/usr/bin/python3
"""Amenity class. Inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class. Inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
