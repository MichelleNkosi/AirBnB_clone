#!/usr/bin/python3
"""Test city Model module"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test city class"""

    def test_public_attributes(self):
        """test default attributes """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
