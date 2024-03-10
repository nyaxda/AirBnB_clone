#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.cmd = HBNBCommand()
        self.patcher = patch('sys.stdout', new=StringIO())
        self.f = self.patcher.start()
        

    def tearDown(self):
        self.patcher.stop()

    def test_default(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("NonExistentCommand")
            self.assertEqual(f.getvalue(), '')

    def test_precmd(self):
        string = "ClassName.method(\"1234-1234-1234\", \"attr\", \"value\")"
        result = self.cmd.precmd(string)
        self.assertEqual(result, string)

    def test_update_dict(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.update_dict(
                "BaseModel", "1234-1234-1234", "{'name': 'John'}")
            self.assertEqual(
                f.getvalue(), "** no instance found **\n")

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cmd.do_EOF(""))

    def test_do_quit(self):
        self.assertTrue(self.cmd.do_quit(""))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            self.assertRegex(
                f.getvalue(), r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n$')

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")


if __name__ == '__main__':
    unittest.main()
