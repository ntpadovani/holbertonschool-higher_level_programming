#!/usr/bin/python3
"""
Imports the function is_same_class
"""


def is_same_class(obj, a_class):
    """
        Returns True if the object is exactly an
        instance of the specified class otherwide
    """
    if a_class is not bool:
        if obj is True or obj is False:
            return False
    if a_class is not object:
        if isinstance(obj, a_class):
            return True
        else:
            return False
    else:
        return False
