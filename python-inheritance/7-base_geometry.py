#!/usr/bin/python3
"""the module which defines base geometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer > 0"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
