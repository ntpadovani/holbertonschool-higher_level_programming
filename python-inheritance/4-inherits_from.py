#!/usr/bin/python3
"""
Imports function that returns true if the object
inherits a class directly or indirectly, otherwise
false
"""


def inherits_from(obj, a_class):
    """
    The inherist_from function
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
