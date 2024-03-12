#!/usr/bin/python3
"""unittest"""

from models.place import Place
import unittest


class Test_place(unittest.TestCase):
    """Test case for Place"""
    def setUp(self):
        """setting up model to test attributes"""
        self.place = Place()
        self.place.name = "My first test"
        self.place.my_number = 98
        self.place.save()

    def test_user_id(self):
        """test place id"""
        print(self.place.id)
        
        self.assertEqual(self.place.name, "My firdt model")

    def test_user_id(self):
        """test place id"""
        self.assertEqual(self.place.my_number, 98)

    def test_instance(self):
        """test case for instance"""
        self.assertIsInstance(self.place.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
