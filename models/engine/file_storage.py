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
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        dict_objs = {}
        for key, obj in FileStorage.__objects.items():
            dict_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dict_objs, f)


    def reload(self):
        """
          deserializes the JSON file to __objects
          (only if the JSON file (__file_path) exists ; otherwise, do nothing.
          If the file doesn't exist, no exception should be raised)
          """

        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict_objs = json.load(f)


            from models.amenity import Amenity
            from models.base_model import BaseModel
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            from models.user import User

            classes = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Place': Place,
                'Amenity': Amenity,
                'Review': Review
            }

            for key, obj_dict in dict_objs.items():
                cls_name, inst_id = key.split('.')
                # fetching class name
                cls = classes[cls_name]
                # creating an object from dictionary
                new_obj = cls(**obj_dict)
                # loading classes instances into __objects as dictionary
                self.new(new_obj)

        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return
