#!/usr/bin/python3
"""Module file_storage :abstracts file storage"""
import json
import os


class FileStorage:
    """(De)Serialize JSON files and load them"""

    # Path to JSON file
    _filepath = "file.json"
    # Dictionary to store objects by id and class name
    _objects = dict()

    def all(self):
        """Returns all _objs in dictionary"""
        return self._objects

    def new(self, obj):
        """Adds new _obj to dictionay"""
        key = str(obj.__class__.__name__ + "." + obj.id)
        json_obj = obj.to_dict()
        self._objects[key] = json_obj

    def save(self):
        """Serialize _obj to JSON"""
        with open(self._filepath, "a") as file:
            json.dump(self._objects, file)

    def reload(self):
        """deserialize JSON to _obj"""
        print("Reload has been called")
        if os.path.isfile(self._filepath):
            print("JSON file exists")
            with open(self._filepath, "r") as file:
                self._objects = json.load(file)
                print("JSON file loaded")
