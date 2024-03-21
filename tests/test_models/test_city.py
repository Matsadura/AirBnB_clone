#!/usr/bin/python3
""" A module that contains test for the user module """
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class tests_City(unittest.TestCase):
    """ A class for testing the City class """

    def test_City(self):
        """ Testing the integrity of City """
        obj = City()
        self.assertTrue(type(obj) is City)
        self.assertIsInstance(obj, City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_AttrsCity(self):
        """ Testing the attributes of City """
        obj = City()

        self.assertIsNotNone(obj.id, True)
        self.assertTrue(type(obj.id) is str)

        self.assertIsNotNone(obj.created_at, True)
        self.assertTrue(type(obj.created_at) is datetime)

        self.assertIsNotNone(obj.updated_at, True)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertIsNotNone(obj.name, True)
        self.assertTrue(type(obj.name) is str)

    def test_Str(self):
        """ Testing the string representation of City """
        obj = City()
        string = f"[City] ({obj.id}) {obj.__dict__}"

        self.assertEqual(str(obj), string)

    def test_Dict(self):
        """ Testing the dictionary representation of City """
        obj = City()
        obj.name = "Meknes"
        dict_rep = obj.to_dict()
        o_create = obj.created_at.isoformat()
        o_update = obj.updated_at.isoformat()
        to_compare = {'id': obj.id, 'created_at': o_create,
                      'updated_at': o_update, 'name': "Meknes",
                      '__class__': 'City'
                      }

        self.assertEqual(dict_rep, to_compare)

        self.assertTrue(type(dict_rep) is dict)

    def tests_Kwargs(self):
        """ Testing creating City instance from a dict_rep """
        dict_rep = {'id': "c123e123-c7d2-4af8-80ef-674f53a4586d",
                    'created_at': "2024-03-21T15:25:35.581256",
                    'updated_at': "2024-03-21T15:25:35.581259",
                    'name': "Meknes", '__class__': 'NaN',
                    }
        obj = City(**dict_rep)

        self.assertEqual(obj.id, "c123e123-c7d2-4af8-80ef-674f53a4586d")
        self.assertTrue(type(obj.id) is str)

        o_create = datetime.fromisoformat("2024-03-21T15:25:35.581256")
        self.assertEqual(obj.created_at, o_create)
        self.assertTrue(type(obj.created_at) is datetime)

        o_update = datetime.fromisoformat("2024-03-21T15:25:35.581259")
        self.assertEqual(obj.updated_at, o_update)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertEqual(obj.name, "Meknes")
        self.assertTrue(type(obj.name) is str)

        self.assertEqual(obj.__class__.__name__, 'City')
