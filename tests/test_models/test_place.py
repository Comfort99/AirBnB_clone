#!/usr/bin/python3
<<<<<<< HEAD

from models.place import Place
# from models import storage
=======
"""unittest"""

from models.place import Place
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
import unittest


class Test_place(unittest.TestCase):
<<<<<<< HEAD
    def setUp(self):
        """ Setting up the model to run for all test """
        self.place = Place()
        self.place.name = "My first model"
=======
    """Test case for Place"""
    def setUp(self):
        """setting up model to test attributes"""
        self.place = Place()
        self.place.name = "My first test"
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
        self.place.my_number = 98
        self.place.save()

    def test_user_id(self):
<<<<<<< HEAD
        print(self.place.id)

        self.assertEqual(self.place.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.place.my_number, 98)

    def test_instance(self):
=======
        """test place id"""
        print(self.place.id)
        
        self.assertEqual(self.place.name, "My firdt model")

    def test_user_id(self):
        """test place id"""
        self.assertEqual(self.place.my_number, 98)

    def test_instance(self):
        """test case for instance"""
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
        self.assertIsInstance(self.place.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
<<<<<<< HEAD

=======
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
