#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_instance(self):
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attribute_values(self):
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')


if __name__ == '__main__':
    unittest.main()
