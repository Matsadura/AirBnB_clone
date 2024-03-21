#!/usr/bin/python3
""" A module that contains test for the user module """
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class tests_Review(unittest.TestCase):
    """ A class for testing the Review class """

    def test_Review(self):
        """ Testing the integrity of Review """
        obj = Review()
        self.assertTrue(type(obj) is Review)
        self.assertIsInstance(obj, Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_AttrsReview(self):
        """ Testing the attributes of Review """
        obj = Review()

        self.assertIsNotNone(obj.id, True)
        self.assertTrue(type(obj.id) is str)

        self.assertIsNotNone(obj.created_at, True)
        self.assertTrue(type(obj.created_at) is datetime)

        self.assertIsNotNone(obj.updated_at, True)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertIsNotNone(obj.text, True)
        self.assertTrue(type(obj.text) is str)

        self.assertIsNotNone(obj.place_id, True)
        self.assertTrue(type(obj.place_id) is str)

        self.assertIsNotNone(obj.user_id, True)
        self.assertTrue(type(obj.user_id) is str)

    def test_Str(self):
        """ Testing the string representation of Review """
        obj = Review()
        string = f"[Review] ({obj.id}) {obj.__dict__}"

        self.assertEqual(str(obj), string)

    def test_Dict(self):
        """ Testing the dictionary representation of Review """
        obj = Review()
        obj.text = "Hello"
        obj.place_id = "Lyon"
        obj.user_id = "Zaoui"
        dict_rep = obj.to_dict()
        o_create = obj.created_at.isoformat()
        o_update = obj.updated_at.isoformat()
        to_compare = {'id': obj.id, 'created_at': o_create,
                      'updated_at': o_update, 'text': "Hello",
                      '__class__': 'Review', 'user_id': "Zaoui",
                      'place_id': "Lyon"
                      }

        self.assertEqual(dict_rep, to_compare)

        self.assertTrue(type(dict_rep) is dict)

    def tests_Kwargs(self):
        """ Testing creating Review instance from a dict_rep """
        dict_rep = {'id': "c123e880-c7d2-4af8-80ef-674f53a4586d",
                    'created_at': "2024-03-21T15:25:35.581256",
                    'updated_at': "2024-03-21T15:25:35.581259",
                    'text': "Zidane", '__class__': 'NaN',
                    'place_id': 'Meknes-1', 'user_id': "Zaoui"
                    }
        obj = Review(**dict_rep)

        self.assertEqual(obj.id, "c123e880-c7d2-4af8-80ef-674f53a4586d")
        self.assertTrue(type(obj.id) is str)

        o_create = datetime.fromisoformat("2024-03-21T15:25:35.581256")
        self.assertEqual(obj.created_at, o_create)
        self.assertTrue(type(obj.created_at) is datetime)

        o_update = datetime.fromisoformat("2024-03-21T15:25:35.581259")
        self.assertEqual(obj.updated_at, o_update)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertEqual(obj.text, "Zidane")
        self.assertTrue(type(obj.text) is str)

        self.assertEqual(obj.place_id, "Meknes-1")
        self.assertTrue(type(obj.place_id) is str)

        self.assertEqual(obj.user_id, "Zaoui")
        self.assertTrue(type(obj.user_id) is str)

        self.assertEqual(obj.__class__.__name__, 'Review')
