#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines a square, inherits from
    Rectangle which inherits from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        super(__class__, self.__class__).width.__set__(self, size)

    def update(self, *args, **kwargs):
        """
        Class that updates the attributes
        of a square Object
        """
        argument = 0
        if args is not None:
            for attr in args:
                if argument == 0:
                    self.id = attr
                elif argument == 1:
                    (super(__class__, self.__class__)
                        .width.__set__(self, attr))
                elif argument == 2:
                    (super(__class__, self.__class__)
                        .x.__set__(self, attr))
                elif argument == 3:
                    (super(__class__, self.__class__)
                        .y.__set__(self, attr))
                argument += 1

        for key in kwargs:
            if key == "id":
                self.id = kwargs.get(key)
            elif key == "size":
                (super(__class__, self.__class__)
                    .width.__set__(self, kwargs.get(key)))
            elif key == "x":
                (super(__class__, self.__class__)
                    .x.__set__(self, kwargs.get(key)))
            elif key == "y":
                (super(__class__, self.__class__)
                    .y.__set__(self, kwargs.get(key)))

    def to_dictionary(self):
        """
        Returns dictionary representation
        of Square object attributes
        """
        dict_repr = {}
        if self.id:
            dict_repr['id'] = self.id
        else:
            dict_repr['id'] = None
        if self.x:
            dict_repr['x'] = self.x
        else:
            dict_repr['x'] = 0
        if self.size:
            dict_repr['size'] = self.width
        else:
            dict_repr['size'] = None
        if self.y:
            dict_repr['y'] = self.y
        else:
            dict_repr['y'] = 0
        return dict_repr
