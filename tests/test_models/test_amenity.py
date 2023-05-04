#!/usr/bin/python3
""" """
import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """."""
        cls.amenity = Amenity(name="water")

    def test_name2(self):
        """ """
        new = self.amenity
        self.assertEqual(type(new.name), str)
