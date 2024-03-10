#!/usr/bin/python3
"""Test state Model module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test state class"""

    def test_public_attributes(self):
        """test default attributes """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
