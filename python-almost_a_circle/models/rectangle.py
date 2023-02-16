#!/usr/bin/python3
"""
Module with class Rectangle
Inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class that defines a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays dimensions of rectangle with #
        """
        for newline in range(self.__y):
            print()
        for hash in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """
        Returns string representation of rectangle
        """
        return (f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')

    def update(self, *args, **kwargs):
        """
        Method to update all attributes of object
        """
        argument = 0
        if args is not None:
            for attr in args:
                if argument == 0:
                    self.id = attr
                elif argument == 1:
                    self.__width = attr
                elif argument == 2:
                    self.__height = attr
                elif argument == 3:
                    self.__x = attr
                elif argument == 4:
                    self.__y = attr
                argument += 1

        for key in kwargs:
            if key == "id":
                self.id = kwargs.get(key)
            elif key == "width":
                self.__width = kwargs.get(key)
            elif key == "height":
                self.__height = kwargs.get(key)
            elif key == "x":
                self.__x = kwargs.get(key)
            elif key == "y":
                self.__y = kwargs.get(key)

    def to_dictionary(self):
        """
        Returns dictionary representation
        of Rectangle object attributes
        """
        dict_repr = {}
        if self.__x:
            dict_repr['x'] = self.__x
        else:
            dict_repr['x'] = 0
        if self.__y:
            dict_repr['y'] = self.__y
        else:
            dict_repr['y'] = 0
        if self.id:
            dict_repr['id'] = self.id
        else:
            dict_repr['id'] = None
        if self.__height:
            dict_repr['height'] = self.__height
        else:
            dict_repr['height'] = None
        if self.__width:
            dict_repr['width'] = self.__width
        else:
            dict_repr['width'] = None
        return dict_repr
