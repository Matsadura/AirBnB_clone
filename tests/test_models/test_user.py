#!/usr/bin/python3
""" A module that contains test for the user module """
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class tests_User(unittest.TestCase):
    """ A class for testing the User class """

    def test_User(self):
        """ Testing the integrity of User """
        obj = User()
        self.assertTrue(type(obj) is User)
        self.assertIsInstance(obj, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_AttrsUser(self):
        """ Testing the attributes of User """
        obj = User()

        self.assertIsNotNone(obj.id, True)
        self.assertTrue(type(obj.id) is str)

        self.assertIsNotNone(obj.created_at, True)
        self.assertTrue(type(obj.created_at) is datetime)

        self.assertIsNotNone(obj.updated_at, True)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertIsNotNone(obj.email, True)
        self.assertTrue(type(obj.email) is str)

        self.assertIsNotNone(obj.password, True)
        self.assertTrue(type(obj.password) is str)

        self.assertIsNotNone(obj.first_name, True)
        self.assertTrue(type(obj.first_name) is str)

        self.assertIsNotNone(obj.last_name, True)
        self.assertTrue(type(obj.last_name) is str)

    def test_Str(self):
        """ Testing the string representation of User """
        obj = User()
        string = f"[User] ({obj.id}) {obj.__dict__}"

        self.assertEqual(str(obj), string)

    def test_Dict(self):
        """ Testing the dictionary representation of User """
        obj = User()
        obj.first_name = "Zidane"
        dict_rep = obj.to_dict()
        o_create = obj.created_at.isoformat()
        o_update = obj.updated_at.isoformat()
        to_compare = {'id': obj.id, 'created_at': o_create,
                      'updated_at': o_update, 'first_name': "Zidane",
                      '__class__': 'User'
                      }

        self.assertEqual(dict_rep, to_compare)

        self.assertTrue(type(dict_rep) is dict)

    def tests_Kwargs(self):
        """ Testing creating User instance from a dict_rep """
        dict_rep = {'id': "c82de880-c7d2-4af8-80ef-674f53a4586d",
                    'created_at': "2024-03-21T15:25:35.581256",
                    'updated_at': "2024-03-21T15:25:35.581259",
                    'first_name': "Zidane", '__class__': 'NaN',
                    'email': "123@gmail.com"
                    }
        obj = User(**dict_rep)

        self.assertEqual(obj.id, "c82de880-c7d2-4af8-80ef-674f53a4586d")
        self.assertTrue(type(obj.id) is str)

        o_create = datetime.fromisoformat("2024-03-21T15:25:35.581256")
        self.assertEqual(obj.created_at, o_create)
        self.assertTrue(type(obj.created_at) is datetime)

        o_update = datetime.fromisoformat("2024-03-21T15:25:35.581259")
        self.assertEqual(obj.updated_at, o_update)
        self.assertTrue(type(obj.updated_at) is datetime)

        self.assertEqual(obj.first_name, "Zidane")
        self.assertTrue(type(obj.first_name) is str)

        self.assertEqual(obj.__class__.__name__, 'User')

        self.assertEqual(obj.email, "123@gmail.com")
        self.assertTrue(type(obj.email) is str)
