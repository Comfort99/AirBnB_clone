#!/usr/bin/python3
"""unittest"""

from models.state import State
import unittest

class Test_state(unittest.TestCase):
    """test cases for state"""
    def setUp(self):
        """setting up models to test attributes"""
        self.state = State()
        self.state.name = "My first model"
        self.state.my_number = 98
        self.state.save()

    def test_state_id(self):
        """test cases for state"""
        print(self.state.id)
        
        self.assertEqual(self.state.name, "My first model")

    def test_state_id(self):
        """test cases for state id"""
        self.assertEqual(self.state.my_number, 98)

    def test_instance(self):
        """test instances"""
        self.assertIsInstance(self.state.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
