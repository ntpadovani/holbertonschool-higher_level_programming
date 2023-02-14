#!/usr/bin/python3
"""
Imports write_file function
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a
    text file (UTF8) and returns the number of
    characters written
    """
    with open(filename, 'w') as file:
        return file.write(text)
