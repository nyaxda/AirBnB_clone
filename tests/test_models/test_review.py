#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_values(self):
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')


if __name__ == '__main__':
    unittest.main()
