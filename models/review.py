#!/usr/bin/python3
"""Review Model module"""
from models.__init__ import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """The state class"""
    place_id = ""
    user_id = ""
    text = ""
