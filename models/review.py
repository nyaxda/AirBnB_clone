#!/usr/bin/python3
"""Review class. Inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class. Inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
