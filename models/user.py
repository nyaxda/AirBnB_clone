#!/usr/bin/python3
"""First User class. Inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class. Inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
