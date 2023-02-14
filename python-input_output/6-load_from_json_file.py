#!/usr/bin/python3
"""
load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"
    """
    with open(filename, 'r') as file:
        JSONstr = file.read()
        return json.loads(JSONstr)
