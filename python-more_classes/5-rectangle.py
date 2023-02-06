#!/usr/bin/python3
"""
This module contains the definition of
a Rectangle class
"""


class Rectangle:
    """Defines a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        printed_rectangle = ""
        for hash in range(self.__height):
            if hash != 0:
                printed_rectangle += "\n"
            for line in range(self.__width):
                printed_rectangle += "#"

        return printed_rectangle

    def __repr__(self):
        return f'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        print("Bye rectangle...")
