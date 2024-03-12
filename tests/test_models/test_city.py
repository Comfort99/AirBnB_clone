#!/usr/bin/python3
"""unittest"""

from models.city import City
import unittest


class Test_city(unittest.TestCase):
    """Test case for city"""
    def setUp(self):
        """setting up model to test attributes"""
        self.city = City()
        self.city.name = "My first Model"
        self.city.my_number = 98
        self.city.save()

    def test_user_id(self):
        """test case for city id"""
        print(self.city.id)
        
        self.assertEqual(self.city.name, "My first model")

    def test_user_id(self):
        """test case for city id"""
        self.assertEqual(self.city.my_number, 98)

    def test_instance(self):
        """instance test"""
        self.assertIsInstance(self.city.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
