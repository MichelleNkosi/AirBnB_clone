#!/usr/bin/python3
"""Module file_storage :abstracts file storage"""
import json
import os


class FileStorage:
    """(De)Serialize JSON files and load them"""

    # Path to JSON file
    __filepath = "file.json"
    # Dictionary to store objects by id and class name
    __objects = dict()

    def all(self):
        """Returns all _objs in dictionary"""
        return self.__objects

    def new(self, obj):
        """Adds new _obj to dictionay"""
        key = str(obj.__class__.__name__ + "." + obj.id)
        json_obj = obj.to_dict()
        self.__objects[key] = json_obj

    def save(self):
        """Serialize _obj to JSON"""
        with open(self.__filepath, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
    """Deserialize JSON to _obj"""
    if os.path.isfile(self.__filepath):
        with open(self.__filepath, "r") as file:
            obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                obj_class = models.classes.get(class_name)
                if obj_class:
                    instance = obj_class(**value)
                    self.__objects[key] = instance
                else:
                    print(f"Error: Class {class_name} not found.")
    else:
        print("Error: File not found.")

