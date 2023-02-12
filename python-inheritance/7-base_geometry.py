#!/usr/bin/python3
"""
Imports class Base Geometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name}' + ' must be greater than 0')
        else:
            self.name = name
            self.value = value
