#!/usr/bin/python3
"""State class. Inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class. Inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
