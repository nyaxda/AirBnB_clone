#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest
from models import storage


class TestStorageModel(unittest.TestCase):
    """testing the file_storage engine"""
    def setUp(self):
        self.ob1 = BaseModel()

    def tearDown(self):
        """delete json file"""
        json_file = storage.path() 
        if os.path.exists(json_file):
            json_abs_path = os.path.abspath(json_file)
            os.remove(json_abs_path)

        storage.clear_objects()

    def test_class_variables(self):
        self.assertTrue(hasattr(storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))

    def test_instances(self):
        self.assertIsInstance(storage, FileStorage)

    def test_all(self):
        obj_dict = storage.all()
        self.assertTrue(isinstance(obj_dict, dict))
        for value in obj_dict.values():
            self.assertIsInstance(value, BaseModel)

    def test_new(self):
        obj1_dict = storage.all()
        self.assertEqual(len(obj1_dict), 1)

        self.ob2 = BaseModel()
        self.ob3 = BaseModel()
        storage.save()

        storage.reload()
        obj_dict3 = storage.all()
        self.assertEqual(len(obj_dict3), 3)
        
    def test_save(self):
        self.assertFalse(os.path.exists(storage.path()))
        self.ob1.save()
        self.assertTrue(os.path.exists(storage.path()))

    def test_reload(self):
        self.assertEqual(len(storage.all()), 1)
        
        obj_dict = storage.all()
        for value in obj_dict.values():
            self.assertTrue(type(value), BaseModel)
