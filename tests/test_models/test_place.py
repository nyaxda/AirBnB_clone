#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_instance(self):
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))

    def test_attribute_values(self):
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, '')


if __name__ == '__main__':
    unittest.main()
