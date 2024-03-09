#!/usr/bin/python3
"""Review class. Inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class. Inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
