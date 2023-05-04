#!/usr/bin/python3
""" """
import unittest
from models.state import State
from models import storage


class test_state(unittest.TestCase):
    """ """

    def setUp(self):
        """."""
        storage.reload()
        self.value = State(name="Lagos")

    def test_name3(self):
        """ """
        new = self.value
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, "Lagos")
        self.assertEqual(new.cities, list())
