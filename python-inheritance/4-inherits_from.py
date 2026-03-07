#!/usr/bin/python3
"""in this module we define inheritance checker function"""


def inherits_from(obj, a_class):

    """in this function we use issubclass function to determine hierarchy"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:  # noqa: E721
        return True
    else:
        return False
