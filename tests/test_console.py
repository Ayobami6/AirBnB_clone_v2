#!/usr/bin/python3

"""Tests for the console output."""

import os
import pathlib as pl
from unittest.mock import patch
from io import StringIO
from unittest import TestCase

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from console import HBNBCommand
from models.engine.file_storage import FileStorage

class TestConsole(TestCase):
    """Console testcase."""

    @classmethod
    def setUpClass(cls):
        """SetUp class."""

        storage.new_object()
        storage.set_path('tests.json')

    @classmethod
    def tearDownClass(cls):
        """tear down class."""

        if pl.Path("file.json").is_file():
            os.remove("file.json")

    def setUp(self):
        """ setUp method for every tests."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="NewYork"')
            self.obj_id = f.getvalue()

            HBNBCommand().onecmd('show State {}'.format(
                self.obj_id))
            self.obj_data = f.getvalue()

    def test_create(self):
        """Tests for do_create method."""

        # checking of object id is in storage
        all_objects = storage.all()

        self.assertIn(
            "State.{}".format(self.obj_id)
            .replace("\n", ""),
            all_objects)

        # checking it the id is in the console output
        self.assertRegex(self.obj_data, self.obj_id.replace("\n", ""))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="EdoState"')
            obj_id = f.getvalue().replace("\n", "")
            HBNBCommand().onecmd('show State {}'.format(obj_id))
            obj_data = f.getvalue()

        # checking if there is a name and it key value
        self.assertRegex(obj_data, "name")
        self.assertRegex(obj_data, "EdoState")


class TestConsoleWithFileStorage(TestCase):

    @classmethod
    def setUpClass(cls):
        """setup class"""
        storage.new_object()
        storage.set_path("test.json")
        
    @classmethod
    def tearDownClass(cls):
        """tear down class."""

        if pl.Path("file.json").is_file():
            os.remove("file.json")

    def test_storage(self):
        """Test is the storage object is the instance object."""
        
        all_objects = storage.all()

        self.assertEqual(len(all_objects), 0)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="EdoState"')
            HBNBCommand().onecmd('create State name="Lagos"')
            HBNBCommand().onecmd('create State name="Imo"')
            HBNBCommand().onecmd('create State name="Delta"')

        all_objects = storage.all()

        self.assertEqual(len(all_objects), 4)