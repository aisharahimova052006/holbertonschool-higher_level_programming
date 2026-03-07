#!/usr/bin/python3
"""we define load from json function in module"""
import json


def load_from_json_file(filename):

    """we use load method to convert to object"""

    with open(filename, 'r') as f:
        data = json.load(f)
        return data
