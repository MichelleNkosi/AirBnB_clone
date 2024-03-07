#!/usr/bin/python3
"""Base Model module"""
from models.__init__ import storage
import datetime
import uuid
date_time = datetime.datetime
genID = uuid.uuid4


class BaseModel:
    """Base class for all AireBnB objects"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        """ OLD CODE. Should be refactored to use kwargs
        self.id = str(genID())
        self.created_at = date_time.now()
        self.updated_at = date_time.now()
        """
        if not kwargs:
            self.id = str(genID())
            self.created_at = date_time.now()
            self.updated_at = date_time.now()
            storage.new(self)

    def __str__(self):
        """How class instance appears when obj is printed"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """Saves the date/time that chanes were maed to instance"""
        storage.save()
        self.updated_at = date_time.now()

    def to_dict(self):
        """Change obj data when saved in dict to readable"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
