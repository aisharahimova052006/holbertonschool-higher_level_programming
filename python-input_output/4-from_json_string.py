#!/usr/bin/python3
"""we define json string to python object converter"""


import json


def from_json_string(my_str):

    """in this function convertion is done by loads method"""

    return json.loads(my_str)
