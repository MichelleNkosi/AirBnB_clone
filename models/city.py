#!/usr/bin/python3
"""City Model module"""
from models.__init__ import storage
from models.base_model import BaseModel


class City(BaseModel):
    """The state class"""
    name = ""
    state_id = ""
