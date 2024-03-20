#!/usr/bin/python3

import json

from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        """ to create a unique FileStorage instance for your application """
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """  
          deserializes the JSON file to __objects
          (only if the JSON file (__file_path) exists ; otherwise, do nothing.
          If the file doesn't exist, no exception should be raised)
          """

        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            return
