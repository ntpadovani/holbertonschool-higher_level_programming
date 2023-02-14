#!/usr/bin/python3
"""
save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using
    JSON representation
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
