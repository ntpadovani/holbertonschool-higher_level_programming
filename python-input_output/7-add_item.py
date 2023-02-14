#!/usr/bin/python3
"""
Script: Adds all arguments to a Python list,
and then saves them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(filename)
except:
    pass
for i in range(1, len(args)):
    my_list.append(args[i])
save_to_json_file(my_list, filename)
