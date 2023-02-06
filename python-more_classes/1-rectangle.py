#!/usr/bin/python3


"""This is a rectangle class"""
class Rectangle:
    """Created a class named Rectangle
    Args:
    width (int): Integers representing the width of a rectangle
    height (int): Integer representing the height of a rectangle
    """

    def __init__(self,width=0,height=0)
        if Type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.width = width
        if Type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.height = height

@property
def width(self):
    return self.__width
@width.setter
    def width(self,value):
    if Type(value) is not int:
        raise TypeError('width must be an integer')
    elif value < 0:
        raise ValueError('width mus be >= 0')
    else:
        return self.width = value
@property
def height(self):
    return self.__height
@height.setter
    def height(self,value):
        if Type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            return self.height = value

