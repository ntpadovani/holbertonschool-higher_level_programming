#!/usr/bin/python3
"""
This is "text_indentation" module
this module contains text_indentation function,
prints a text with 2 new lines after each of these
characters: '.', '?' and ':'
"""


def text_indentation(text):
    """Return string divided by spaces
    Arguments:
        text (string): string to be formmated
    raises:
        TypeError: if the text called with the program is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    count = ":"
    for c in text:
        if c is " " and count in ".?:":
            continue
        print(c, end="")
        if c in ".:?":
            print("\n")
        count = c
