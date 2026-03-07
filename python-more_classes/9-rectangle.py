#!/usr/bin/python3
"""we define a rectangle class here"""


class Rectangle:
    """a simple rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width != 0 and self.__height != 0:
            return 2*(self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            pass
        string = ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string += str(self.print_symbol)
            if i == self.__height - 1:
                pass
            else:
                string += '\n'
        return string

    def __repr__(self):
        code = f"Rectangle({self.__width}, {self.__height})"
        eval(code)
        return code

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            pass
        area_1 = rect_1.__width * rect_2.__height
        area_2 = rect_2.__width * rect_2.__height
        if area_1 > area_2:
            return rect_1
        elif area_1 < area_2:
            return rect_2
        elif area_1 == area_2:
            return rect_1
        else:
            pass

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
