#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attribute_values(self):
        self.assertEqual(self.amenity.name, '')


if __name__ == '__main__':
    unittest.main()
