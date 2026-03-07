#!/usr/bin/python3
"""we define file writing function in this module"""


def write_file(filename='', text=''):
    """we write to file using write method"""
    with open(filename, 'w') as f:
        return f.write(text)
