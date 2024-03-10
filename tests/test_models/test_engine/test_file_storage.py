#!/usr/bin/python3
"""test_file_starage.py: Module for unit testing the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Creat these objs before each test methode"""
        self.file_storage = FileStorage()
        self.base_obj = BaseModel()
        self.base_obj.id = "123"
        self.file_path = "file.json"

    def tearDown(self):
        """Fufile these commands after each test is done"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new__and_all_methods(self):
        """Checks if new object is added to _objects dictionary"""
        test_dict = {'id': '123',
                     'created_at': '2022-02-21T12:00:00',
                     'updated_at': '2022-02-21T12:00:00'}
        self.file_storage.new(self.base_obj)
        self.assertIn('BaseModel.123', self.file_storage.all())

    def test_save_method(self):
        """Add _objects dictionary to JSON file"""
        test_dict = {'id': '123', 'created_at': '2022-02-21T12:00:00',
                     'updated_at': '2022-02-21T12:00:00',
                     '__class__': 'BaseModel'}
        self.file_storage._objects = {'BaseModel.123': test_dict}
        # Save objects to file
        self.file_storage.save()
        # Check if file exists
        self.assertTrue(os.path.exists(self.file_path))
        # Check if file contains the _objects dictionary
        with open(self.file_path, 'r') as file:
            contents = file.read()
        self.assertIn('__class__', contents)

    def test_reload_method(self):
        """Create a file with sample data"""
        with open(self.file_path, "w") as file:
            test_dict = '{"BaseModel.123":\
            {"id": "123", "created_at": "2022-02-21T12:00:00",\
             "updated_at": "2022-02-21T12:00:00"}}'
            file.write(test_dict)
        # Reload data from file
        self.file_storage.reload()
        # Check if data is loaded into _objects dictionary
        self.assertIn('BaseModel.123', self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
