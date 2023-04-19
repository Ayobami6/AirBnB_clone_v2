#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from unittest.mock import patch
import pathlib as pl
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


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        # from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    # @patch('models.engine.file_storage.FileStorage._FileStorage__objects',
    #        {'ClassName.id1': 'object1', 'ClassName.id2': 'object2',
    #        'OtherClassName.id1': 'object3', 'OtherClassName.id2': 'object4'})
    def test_all_with_cls(self):
        file_storage = FileStorage()
        ClassName = 'ClassName.id1'.split('.')[0]
        result = file_storage.all(cls=type(ClassName))
        self.assertEqual(
            result, {})

    @patch('models.engine.file_storage.FileStorage._FileStorage__objects',
           {'ClassName.id1': 'object1', 'ClassName.id2': 'object2',
            'OtherClassName.id1': 'object3', 'OtherClassName.id2': 'object4'})
    def test_all_without_cls(self):
        file_storage = FileStorage()
        result = file_storage.all()
        self.assertEqual(result, {'ClassName.id1': 'object1',
                                  'ClassName.id2': 'object2',
                                  'OtherClassName.id1': 'object3',
                                  'OtherClassName.id2': 'object4'})


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

        storage.set_path("file.json")
        if pl.Path("tests.json").is_file():
            os.remove("tests.json")

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
            HBNBCommand().onecmd('create State name="Edo State"')
            obj_id = f.getvalue().replace("\n", "")
            HBNBCommand().onecmd('show State {}'.format(obj_id))
            obj_data = f.getvalue()

        # checking if there is a name and it key value
        self.assertRegex(obj_data, "name")
        self.assertRegex(obj_data, "Edo State")

    def test_multiple_parameters(self):
        """testing for multiple name parameters."""

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create User name="Jojo" sprint=3' +
                                 ' state="Edo State"')
            user_id = f.getvalue().replace("\n", "")

            HBNBCommand().onecmd('show User {}'.format(user_id))
            user_data = f.getvalue().replace("\n", "")

            # check if user_id is in the console response
            self.assertRegex(user_data, user_id)

            # checking if object exist in the storage class
            all_objects = storage.all()
            self.assertIn("User.{}".format(user_id),
                          all_objects)
            user_object = all_objects['User.{}'.format(user_id)]

            self.assertIn("name", user_object.__dict__)
            self.assertIn("sprint", user_object.__dict__)
            self.assertIn("state", user_object.__dict__)

            self.assertIsInstance(getattr(user_object, 'name'), str)
            self.assertIsInstance(getattr(user_object, 'sprint'), int)
            self.assertIsInstance(getattr(user_object, 'state'), str)


class TestConsoleWithFileStorage(TestCase):

    @classmethod
    def setUpClass(cls):
        """setup class"""
        storage.new_object()
        storage.set_path("tests.json")

    @classmethod
    def tearDownClass(cls):
        """tear down class."""

        storage.set_path("file.json")
        if pl.Path("tests.json").is_file():
            os.remove("tests.json")

    def test_storage(self):
        """Test is the storage object is the instance object."""

        all_objects = storage.all()

        self.assertEqual(len(all_objects), 0)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Edo State"')
            HBNBCommand().onecmd('create State name="Lagos"')
            HBNBCommand().onecmd('create State name="Imo"')
            HBNBCommand().onecmd('create State name="Delta"')

        all_objects = storage.all()

        self.assertEqual(len(all_objects), 4)
