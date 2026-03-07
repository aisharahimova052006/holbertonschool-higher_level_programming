#!/usr/bin/python3
"""the module which defines square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        return self.__height*self.__width

    def __str__(self):
        return (f"[Square] {self.__width}/{self.__height}")
