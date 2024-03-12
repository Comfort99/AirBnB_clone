#!/usr/bin/python3
<<<<<<< HEAD

from models.city import City
# from models import storage
=======
"""unittest"""

from models.city import City
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
import unittest


class Test_city(unittest.TestCase):
<<<<<<< HEAD
    def setUp(self):
        """ Setting up the model to run for all test """
        self.city = City()
        self.city.name = "My first model"
=======
    """Test case for city"""
    def setUp(self):
        """setting up model to test attributes"""
        self.city = City()
        self.city.name = "My first Model"
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
        self.city.my_number = 98
        self.city.save()

    def test_user_id(self):
<<<<<<< HEAD
        print(self.city.id)

        self.assertEqual(self.city.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.city.my_number, 98)

    def test_instance(self):
=======
        """test case for city id"""
        print(self.city.id)
        
        self.assertEqual(self.city.name, "My first model")

    def test_user_id(self):
        """test case for city id"""
        self.assertEqual(self.city.my_number, 98)

    def test_instance(self):
        """instance test"""
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
        self.assertIsInstance(self.city.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
<<<<<<< HEAD

=======
>>>>>>> dcb4e2333bbaac5eea5e5e9fb64ec1d72635e29f
