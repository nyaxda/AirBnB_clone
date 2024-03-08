#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestStorageModel(unittest.TestCase):
    """testing the file_storage engine"""
    def setUp(self):
        self.ob1 = BaseModel()
        self.store1 = FileStorage()

    def tearDown(self):
        """delete json file"""
        json_file = self.store1.path() 
        if os.path.exists(json_file):
            json_abs_path = os.path.abspath(json_file)
            os.remove(json_abs_path)

        self.store1.clear_objects()

    def test_class_variables(self):
        self.assertTrue(hasattr(self.store1, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.store1, '_FileStorage__objects'))

    def test_instances(self):
        self.assertIsInstance(self.store1, FileStorage)

    def test_all(self):
        obj_dict = self.store1.all()
        self.assertTrue(isinstance(obj_dict, dict))
        for value in obj_dict.values():
            self.assertIsInstance(value, BaseModel)

    def test_new(self):
        obj_dict1 = self.store1.all()
        self.assertEqual(len(obj_dict1), 1)

        self.ob2 = BaseModel()
        self.ob3 = BaseModel()
        self.store3 = FileStorage()

        obj_dict3 = self.store3.all()
        self.assertEqual(len(obj_dict3), 3)
        
    def test_save(self):
        self.assertFalse(os.path.exists(self.store1.path()))
        self.ob1.save()
        self.assertTrue(os.path.exists(self.store1.path()))

    def test_reload(self):
        self.assertEqual(len(self.store1.all()), 1)
        
        obj_dict = self.store1.all()
        for value in obj_dict.values():
            self.assertTrue(type(value), BaseModel)
