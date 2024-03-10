#!/usr/bin/python3
"""Test state Model module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test review class"""

    def test_public_attributes(self):
        """test default attributes """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
