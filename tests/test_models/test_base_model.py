#!/usr/bin/python3
"""test_base_module
Module for unit testsing the base Model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.__init__ import storage
import os


class TestBaseModel(unittest.TestCase):
    """Test the Base Model"""

    def setUp(self):
        """Creat BaseModel obj before each test methode"""
        self.model = BaseModel()

    def tearDown(self):
        """Run at the end of test"""
        if os.path.exists("~/AirBnB_clone/file.json"):
            os.remove("file.json")

    def test_id_generation_exists(self):
        """Check if id is correct type"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertIsInstance(self.model.id, str)

    def test_created_at_exists(self):
        """Check if created_at is correct type"""
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_exists(self):
        """Check if updated_at is correct type"""
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Check if updated_at is changed after calling save"""
        oldupdate = self.model.updated_at
        self.model.save()
        self.assertNotEqual(oldupdate, self.model.updated_at)

    def test_to_dict(self):
        """Check if to_dict returns the right keys in a dictionary"""
        self.assertTrue(hasattr(self.model, 'to_dict'))
        self.assertIsInstance(self.model.to_dict(), dict)

        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(set(self.model.to_dict().keys()), set(expected_keys))

    def test_str_representation(self):
        """Check string representtion of BaseModel"""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id,
                                                    self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
