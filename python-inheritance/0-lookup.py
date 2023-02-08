#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    Args:
    obj: a literal object
    Return:
    list of available attributes and methods of an object
    """
    return dir(obj)