#!/usr/bin/python3

from models.amenity import Amenity
# from models import storage
"""unittest"""

from models.amenity import Amenity
import unittest


class Test_amenity(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.amenity = Amenity()
    """Test case Class for amenity"""
    def setUp(self):
        """Setting up model for testing attributes"""
        self.amenity = Amenity
        self.amenity.name = "My first model"
        self.amenity.my_number = 98
        self.amenity.save()

    def test_user_id(self):
        print(self.amenity.id)

        self.assertEqual(self.amenity.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.amenity.my_number, 98)

    def test_instance(self):
        """Test case for amenity id"""
        print(self.amenity.id)
        
        self.assertEqual(self.amenity.name, "My first model")

    def test_amenity_id(self):
        """Test case for amenity"""
        self.assertEqual(self.amenity.my_number, 98)

    def test_instance(self):
        """test case for instance"""
        self.assertIsInstance(self.amenity.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
<<<<<<< HEAD

=======
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
