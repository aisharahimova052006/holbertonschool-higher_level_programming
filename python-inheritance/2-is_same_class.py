#!/usr/bin/python3
"""in this module we define is_same_class function"""


def is_same_class(obj, a_class):

    """in this function we use isinstance to detect class"""

    if isinstance(obj, a_class) and type(obj) == a_class:  # noqa: E721
        return True
    else:
        return False
