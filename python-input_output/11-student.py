#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            my_dict = {}
            for i in attrs:
                if str(i) == "first_name":
                    my_dict[i] = self.first_name
                elif i == "last_name":
                    my_dict[i] = self.last_name
                elif i == "age":
                    my_dict[i] = self.age
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            elif key == "last_name":
                self.last_name = value
            elif key == "age":
                self.age = value
