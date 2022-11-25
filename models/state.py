#!/usr/bin/python3
"""
This is 'state' module.
Functions and Classes:
    class State(BaseModel):
"""


from models.base_model import BaseModel


class State(BaseModel):
    """representing a state"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
