#!/usr/bin/python3
"""
    A module that contains the class FileStorage
"""
import json
import os
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


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
        # self.__objects[f"{obj.__class__.__name__}." + obj.id] = obj.to_dict()
        self.__objects.update({f"{obj.__class__.__name__}." + obj.id: obj})
        # self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
            A public instance method that serializes __objects
            to the JSON file (path: __file_path)
        """
        tmp = {}
        for key in self.__objects:
            tmp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(tmp, f)
        # print(self.__objects)

    def reload(self):
        """
            A public instance method that deserializes the JSON file to
            __objects (only if the JSON file exits otherwise it does nothing)
        """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                tmp = json.load(f)
            for key in tmp:
                self.__objects[key] = classes[tmp[key]["__class__"]](**tmp[key])
                # print(self.__objects)
