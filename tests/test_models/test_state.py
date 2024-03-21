#!/usr/bin/python3
""" A module that contains test for the user module """
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class tests_State(unittest.TestCase):
    """ A class for testing the State class """

    def test_State(self):
        """ Testing the integrity of State """
        obj = State()
        self.assertTrue(type(obj) is State)
        self.assertIsInstance(obj, State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_AttrsState(self):
        """ Testing the attributes of State """
        obj = State()

        self.assertIsNotNone(obj.id, True)
        self.assertTrue(type(obj.id) is str)

        self.assertIsNotNone(obj.created_at, True)
        self.assertTrue(type(obj.created_at) is datetime)

        self.assertIsNotNone(obj.updated_at, True)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertIsNotNone(obj.name, True)
        self.assertTrue(type(obj.name) is str)

    def test_Str(self):
        """ Testing the string representation of State """
        obj = State()
        string = f"[State] ({obj.id}) {obj.__dict__}"

        self.assertEqual(str(obj), string)

    def test_Dict(self):
        """ Testing the dictionary representation of State """
        obj = State()
        obj.name = "Zidane"
        dict_rep = obj.to_dict()
        o_create = obj.created_at.isoformat()
        o_update = obj.updated_at.isoformat()
        to_compare = {'id': obj.id, 'created_at': o_create,
                      'updated_at': o_update, 'name': "Zidane",
                      '__class__': 'State'
                      }

        self.assertEqual(dict_rep, to_compare)

        self.assertTrue(type(dict_rep) is dict)

    def tests_Kwargs(self):
        """ Testing creating State instance from a dict_rep """
        dict_rep = {'id': "c123e880-c7d2-4af8-80ef-674f53a4586d",
                    'created_at': "2024-03-21T15:25:35.581256",
                    'updated_at': "2024-03-21T15:25:35.581259",
                    'name': "Zidane", '__class__': 'NaN',
                    }
        obj = State(**dict_rep)

        self.assertEqual(obj.id, "c123e880-c7d2-4af8-80ef-674f53a4586d")
        self.assertTrue(type(obj.id) is str)

        o_create = datetime.fromisoformat("2024-03-21T15:25:35.581256")
        self.assertEqual(obj.created_at, o_create)
        self.assertTrue(type(obj.created_at) is datetime)

        o_update = datetime.fromisoformat("2024-03-21T15:25:35.581259")
        self.assertEqual(obj.updated_at, o_update)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertEqual(obj.name, "Zidane")
        self.assertTrue(type(obj.name) is str)

        self.assertEqual(obj.__class__.__name__, 'State')
