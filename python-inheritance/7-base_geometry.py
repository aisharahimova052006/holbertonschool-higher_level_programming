#!/usr/bin/python3
"""Module that defines BaseGeometry class with integer validation"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, *args):
        """Validates value is an integer > 0

        Expected arguments: (name, value)
        """
        if len(args) != 2:
            raise TypeError(
                "integer_validator() missing 2 required positional "
                "arguments: name and value"
            )

        name, value = args

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
