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
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(genID())
        self.created_at = date_time.now()
        self.updated_at = date_time.now()
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = date_time.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        """How class instance appears when obj is printed"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """Saves the date/time that changes were made to instance"""
        key = str(self.__class__.__name__ + "." + self.id)
        storage.delete(key)        
        self.updated_at = date_time.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Change obj data when saved in dict to readable"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
