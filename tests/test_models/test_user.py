#!/usr/bin/python3
<<<<<<< HEAD
=======
"""unittesst"""
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f

from models.user import User
from models import storage
import unittest


class Test_user(unittest.TestCase):
<<<<<<< HEAD
    def setUp(self):
        """ Setting up the model to run for all test """
        self.user = User()
        self.user.name = "My first model"
=======
    """Test case for user"""
    def setUp(self):
        """setting uo test cases for attributes"""
        self.user = User()
        self.user.name = "My first Model"
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
        self.user.my_number = 98
        self.user.save()

    def test_user_id(self):
<<<<<<< HEAD
        print(self.user.id)

        self.assertEqual(self.user.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.user.my_number, 98)

    def test_instance(self):
=======
        """test case for user id"""
        print(self.user.id)
        
        self.assertEqual(self.user.name, "My first model")

    def test_user_id(self):
        """user id test case"""
        self.assertEqual(self.user.my_number, 98)

    def test_instance(self):
        """test case for instances"""
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
        self.assertIsInstance(self.user.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
