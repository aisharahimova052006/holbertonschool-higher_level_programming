#!/usr/bin/python3
"""in this module we define is_same_class function"""


def is_kind_of_class(obj, a_class):

    """in this function we use isinstance to detect class"""

    if isinstance(obj, a_class) and issubclass(type(obj), a_class):  # noqa: E721
        return True
    else:
        return False
