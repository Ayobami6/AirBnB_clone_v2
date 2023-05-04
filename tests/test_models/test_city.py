#!/usr/bin/python3
""" """
import unittest
from models.city import City
from models.state import State


class test_City(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """."""
        cls.state = State(name="Edo_State")
        cls.city = City(name="Benin_City", state_id=cls.state.id)

    def test_state_id(self):
        """ """
        new = self.city
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.city
        self.assertEqual(type(new.name), str)

    def test_foreign_key(self):
        """ """
        state = self.state
        city = self.city
        self.assertEqual(city.state_id, state.id)
