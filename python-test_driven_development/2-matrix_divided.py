#!/usr/bin/python3


"""
This is "2-matrix_divided" module
this module contains add_integers function
that that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """[print the full name]
    Arguments:
        matrix {[lis]} -- [description]
        div {[type]} -- [description]
    Raises:
        TypeError: [matrix must be a matrix
         (list of lists) of integers/floats]
        ZeroDivisionError: [division by zero]
        TypeError: [Each row of the matrix must have the same size]
        TypeError: [div must be a number]
    Returns:
        [type] -- [description]
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    if len(matrix[0]) is 0:
        raise TypeError(err1)

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError(err2)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(err1)

    if type(div) not in (int, float):
        raise TypeError(err3)

    if div is 0:
        raise ZeroDivisionError(err4)

    return [[round((elem / div), 2) for elem in row] for row in matrix]
