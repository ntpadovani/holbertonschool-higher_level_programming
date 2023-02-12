#!/usr/bin/python3
"""
This module imports a function that returns
the list of available attributes and methods of
an object
"""


def lookup(obj):
    """
    Returns list of available attributes and
    methods of an object
        Args:
            obj (unknown type): object to verify
    """
    return dir(obj)
