#!/usr/bin/python3
"""we define module"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

arguments = []
try:
    list2 = load('add_item.json')
    arguments.extend(list2)
except FileNotFoundError:
    pass
arguments.extend(sys.argv[1:])
save(arguments, 'add_item.json')
