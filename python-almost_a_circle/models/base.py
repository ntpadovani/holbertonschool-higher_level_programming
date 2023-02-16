#!/usr/bin/python3
"""
Module with Class 'Base'
"""
import json


class Base:
    """
    'base' of all the other classes in this project,
    the goal is to manage id attribute in all future
    classes and avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f'{cls.__name__}.json'
        with open(filename, 'w') as file:
            list_to_save = []
            if list_objs is None:
                file.write(cls.to_json_string(list_to_save))
            else:
                for list_dict in list_objs:
                    list_to_save.append(list_dict.to_dictionary())
                file.write(cls.to_json_string(list_to_save))

    @staticmethod
    def from_json_string(json_string):
        list_to_return = []
        if json_string is None:
                return list_to_return
        else:
            list_to_return = json.loads(json_string)
            return list_to_return

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            instance = cls(1)
        elif cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        cls.update(instance, **dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Be careful with this function, if an error
        occurs
        """
        filename = f'{cls.__name__}.json'
        list_of_instances = cls.from_json_string(None)
        try:
            with open(filename, 'r') as file:
                dict_of_attrs = json.load(file)
            for dict in dict_of_attrs:
                list_of_instances.append(cls.create(**dict))
        except Exception:
            return []
        else:
            return list_of_instances
