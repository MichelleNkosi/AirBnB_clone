#!/usr/bin/python3
"""Amenity Model module"""
from models.__init__ import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The state class"""
    name = ""
