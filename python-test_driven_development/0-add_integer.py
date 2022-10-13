#!/usr/bin/python3
"""
This is "0-add_integer" module
this module contains add_integers function that adds two integers
"""


def add_integer(a, b=98):
    """adds 2 integers.
    Arguments:
        a {[int]} -- [description]
    Keyword Arguments:
        b {int} -- [description] (default: {98})
    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]
    Returns:
        [int] -- [addition of a and b]
    """
    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return a + b
