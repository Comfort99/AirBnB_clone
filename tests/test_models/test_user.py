#!/usr/bin/python3
"""unittesst"""

from models.user import User
from models import storage
import unittest


class Test_user(unittest.TestCase):
    """Test case for user"""
    def setUp(self):
        """setting uo test cases for attributes"""
        self.user = User()
        self.user.name = "My first Model"
        self.user.my_number = 98
        self.user.save()

    def test_user_id(self):
        """test case for user id"""
        print(self.user.id)
        
        self.assertEqual(self.user.name, "My first model")

    def test_user_id(self):
        """user id test case"""
        self.assertEqual(self.user.my_number, 98)

    def test_instance(self):
        """test case for instances"""
        self.assertIsInstance(self.user.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
