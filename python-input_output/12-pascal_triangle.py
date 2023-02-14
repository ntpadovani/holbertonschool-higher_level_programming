#!/usr/bin/python3
"""
pascal_triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing pascals triangle
    """
    the_list = []
    count = 2
    for i in range(n):
        a_list = []
        num = 1
        for j in range(1, count):
            a_list.append(num)
            num *= i
            
        the_list.append(a_list)
        count += 1
    return the_list
