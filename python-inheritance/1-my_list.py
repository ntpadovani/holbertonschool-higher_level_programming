#!/usr/bin/python3
"""This is a MyList class that is inherited"""


class MyList(list):
    """
    A class that inherits from list
    Attributes: None
    """

    def print_sorted(self):
        """Prints a sorted list of ints"""

        print(sorted(self))
