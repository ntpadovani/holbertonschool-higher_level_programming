#!/usr/bin/python3
"""
Imports append_write function
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of
    a file (UTF8) and returns number of characters
    """
    with open(filename, 'a') as file:
        return file.write(text)
