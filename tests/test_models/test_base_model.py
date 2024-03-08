#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test fixtures"""
        self.tester = BaseModel()

    def test_initialization(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.tester, BaseModel)
        self.assertTrue(hasattr(self.tester, 'id'))
        self.assertTrue(hasattr(self.tester, 'created_at'))
        self.assertTrue(hasattr(self.tester, 'updated_at'))
        self.assertIsInstance(self.tester.created_at, datetime)
        self.assertIsInstance(self.tester.updated_at, datetime)
        self.assertEqual(type(self.tester.id), str)

    def test_str_method(self):
        """Test __str__ method"""
        expected_str = "[BaseModel] ({}) {}".format(
            self.tester.id, self.tester.__dict__)
        self.assertEqual(str(self.tester), expected_str)

    def test_save_method(self):
        """Test save method"""
        initial_updated_at = self.tester.updated_at
        self.tester.save()
        self.assertNotEqual(self.tester.updated_at, initial_updated_at)
        self.assertIsInstance(self.tester.updated_at, datetime)

    def test_to_dict_method(self):
        """Test to_dict method"""
        tester_dict = self.tester.to_dict()
        self.assertEqual(tester_dict['id'], self.tester.id)
        self.assertEqual(tester_dict['__class__'], 'BaseModel')
        self.assertIsInstance(tester_dict['created_at'], str)
        self.assertEqual(
            tester_dict['created_at'], self.tester.created_at.isoformat())
        self.assertIsInstance(tester_dict['updated_at'], str)
        self.assertEqual(
            tester_dict['updated_at'], self.tester.updated_at.isoformat())
