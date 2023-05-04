#!/usr/bin/python3

import unittest
from os import environ
from unittest.mock import patch
from io import StringIO
import MySQLdb
from sqlalchemy.orm.exc import UnmappedInstanceError

from models.state import State
from models.city import City
from models import storage
from models.base_model import Base, BaseModel
from console import HBNBCommand


@unittest.skipUnless(environ.get("HBNB_TYPE_STORAGE") == "db",
                     "skip when using filestorage")
class TestConsoleDatabase(unittest.TestCase):
    """Tests when storage type db."""

    @classmethod
    def setUpClass(cls):
        """Sets up class before running any tests."""
        HOST = environ.get("HBNB_MYSQL_HOST")
        USER = environ.get("HBNB_MYSQL_USER")
        PWD = environ.get("HBNB_MYSQL_PWD")
        DB = environ.get("HBNB_MYSQL_DB")
        cls.db_con = MySQLdb.connect(user=USER, password=PWD, host=HOST,
                                     database=DB)

    def setUp(self):
        """To set the needed things for every test."""
        storage.reload()

    def tearDown(self):
        """Run for cleanup on eery test."""
        cursor = self .db_con.cursor()

        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute("DROP TABLE cities;DROP TABLE states")
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        cursor.close()

    def test_create(self):
        """Test HBNB console create.

        tests if a new record is created on the database.
        """
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("create State name=\"Edo\"")

            cursor = self.db_con.cursor()
            cursor.execute("SELECT * FROM states")
            data = cursor.fetchall()
            cursor.close()

        self.assertEqual(len(data), 1)

    def test_arguments(self):
        """Test if the passed arguments are there."""
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("create State name=\"Delta_State\"")
            # getting the id of the state newly created from the console
            state_id = out.getvalue().strip('\n')
            # creating an new city with the and setting the state_id column
            # to the one we just created
            cmds = 'create City state_id="{}" name="warri"'.format(
                str(state_id))
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd(cmds)
            city_id = out.getvalue().replace('\n', '')

        cursor = self.db_con.cursor()
        cursor.execute("SELECT * FROM cities")
        data = cursor.fetchall()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][0], "warri")
        self.assertEqual(data[0][1], state_id)
        self.assertEqual(city_id, data[0][2])

        cursor.execute("SELECT * FROM states")
        data = cursor.fetchall()

        self.assertEqual("Delta State", data[0][0])
        self.assertEqual(state_id, data[0][1])


@unittest.skipUnless(environ.get("HBNB_TYPE_STORAGE") == "db",
                     "skip when using filestorage")
class TestDBStorage(unittest.TestCase):
    """."""

    @classmethod
    def setUpClass(cls):
        """Sets up class before running any tests."""
        HOST = environ.get("HBNB_MYSQL_HOST")
        USER = environ.get("HBNB_MYSQL_USER")
        PWD = environ.get("HBNB_MYSQL_PWD")
        DB = environ.get("HBNB_MYSQL_DB")
        cls.db_con = MySQLdb.connect(user=USER, password=PWD, host=HOST,
                                     database=DB)

    def setUp(self):
        """To set the needed things for every test."""
        storage.reload()

    def tearDown(self):
        """Run for cleanup on eery test."""
        cursor = self .db_con.cursor()

        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute("DROP TABLE cities;DROP TABLE states")
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        cursor.close()

    def test_basemodel(self):
        """."""
        with self.assertRaises(AttributeError and UnmappedInstanceError):
            new = BaseModel()
            new.save()

