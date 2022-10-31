#!/usr/bin/python3
"""
   this contains the filestorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    class attributes
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for k, v in self.__objects.items():
            obj_dict[k] = v.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                dict_obj = json.load(f)
            for k, v in dict_obj.items():
                """here can use one of this functions"""
                """self.__objects[k] = eval(v['__class__'])(**v)"""
                self.__objects[k] = eval(k.split(".")[0])(**v)
        except FileNotFoundError:
            pass
