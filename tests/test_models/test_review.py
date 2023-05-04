#!/usr/bin/python3
""" """
import unittest
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.place import Place


class test_review(unittest.TestCase):
    """ """

    def setUp(self):
        """ """
        state = State(name="Edo_State")
        city = City(name="Benin_City", state_id=state.id)
        user = User(first_name="Jojo", last_name="Thomas",
                    email="jojothomas1515@gmail.com",
                    password="hahahahaha")
        self.place = Place(city_id=city.id, user_id=user.id,
                           name="The_Hotel",
                           description="hihihihi",
                           number_rooms=11,
                           number_bathrooms=24,
                           max_guest=5,
                           price_by_night=1000,
                           latitude=-12345,
                           longitude=1212.233,
                           )

        self.value = Review(place_id=self.place.id, user_id=user.id,
                            text="hello man")

    def test_place_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value
        self.assertEqual(type(new.text), str)

    def text_relationship(self):
        """."""
        new = self.value
        self.assertEqual(new.place_id, self.place.id)
