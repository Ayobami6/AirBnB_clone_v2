#!/usr/bin/python3
""" """
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """ """

    def setUp(self):
        """."""
        self.value = User(**{"first_name": "joseph",
                             "last_name": "thomas",
                             "email": "jojothomas@example.com",
                             "password": "qwerty"})

    def test_first_name(self):
        """ """
        new = self.value
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value
        self.assertEqual(type(new.password), str)
