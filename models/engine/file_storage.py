#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        # New temp to store all class
        new_dict = {}
        data_dict = self.__objects
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            for key in data_dict.keys():
                # remove the . from te key
                key_dot_stripped = key.replace(".", " ")
                # new key array
                new_key = key_dot_stripped.split()
                # if class name is same as name in the key
                if (cls.__name__ == new_key[0]):
                    new_dict[key] = self.__objects[key]
            return new_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete an objects

        Args:
            obj (None, optional): class object
        """
        if obj:
            # get key
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ Reloads storage
        """
        self.reload()

    @classmethod
    def set_path(cls, file_path: str):
        """To change the save file path."""
        cls.__file_path = file_path

    @classmethod
    def new_object(cls):
        """Object storage."""
        cls.__objects = {}
