#!/usr/bin/python3
"""Module for abstracting file storage"""

import json
import os

class FileStorage:
    """(De)Serialize JSON files and load them"""

    #Path to JSON file
    _filepath = "/AirBnB_clone/file.json"
    #Dictionary to store objects by id and class name
    _objects = dict()

    def all(self):
        """Returns all _objs in dictionary"""
        return self._objects

    def new(self, obj):
        """Adds new _obj to dictionay"""
        key = str( obj.__class__.__name__ + "." + obj.id )
        self._objects[key] = obj

    def save(self):
        """Serialize _obj to JSON"""
        with open(self._filepath, "a") as file:
            json.dump(self._objects, file)

    def reload(self):
        """deserialize JSON to _obj"""
        if os.path.isfile(self._filepath):
            with open(self._filepath, "r") as file:
                self._objects = json.load(file)
