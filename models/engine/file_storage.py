#!/usr/bin/python3
"""
    A module that contains the class FileStorage
"""
import json
import os


class FileStorage():
    """
        A class that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            A public instance method that returns the dictrionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            A public instance method that sets in __objects the Obj
            with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}." + obj.id] = obj.to_dict()

    def save(self):
        """
            A public instance method that serializes __objects
            to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
            A public instance method that deserializes the JSON file to
            __objects (only if the JSON file exits otherwise it does nothing)
        """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.load(f)
