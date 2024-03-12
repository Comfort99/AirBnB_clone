#!/usr/bin/python3
"""unittest"""

from models.amenity import Amenity
import unittest


class Test_amenity(unittest.TestCase):
    """Test case Class for amenity"""
    def setUp(self):
        """Setting up model for testing attributes"""
        self.amenity = Amenity
        self.amenity.name = "My first model"
        self.amenity.my_number = 98
        self.amenity.save()

    def test_user_id(self):
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
