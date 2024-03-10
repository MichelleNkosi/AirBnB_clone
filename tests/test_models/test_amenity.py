#!/usr/bin/python3
"""Test amenity Model module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test amenity class"""

    def test_public_attributes(self):
        """test default attributes """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
