#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance(self):
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_values(self):
        self.assertEqual(self.state.name, '')


if __name__ == '__main__':
    unittest.main()
