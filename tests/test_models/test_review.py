#!/usr/bin/python3
"""unittest"""
from models.review import Review
import unittest


class Test_review(unittest.TestCase):
    """test case =s for review"""
    def setUp(self):
        """Setting up model to test attributes"""
        self.review = Review()
        self.review.name = "My first model"
        self.review.my_number = 98
        self.review.save()

    def test_user_id(self):
        """test case for review id"""
        print(self.review.id)
        
        self.assertEqual(self.review.name, "My first model")

    def test_user_id(self):
        """test case for review"""
        self.assertEqual(self.review.my_number, 98)

    def test_instance(self):
        """test instances"""
        self.assertIsInstance(self.review.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
