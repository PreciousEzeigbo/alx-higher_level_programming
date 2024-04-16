#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """The function that divides all elements of a matrix
    Attributes:
        matrix: a list of integers/floats
        div: the number that divides the elements
    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats.
                If all rows of `matrix` are not of the same size.
                If `div` is not a number (integer or float).
        ZeroDivisionError: if equal to 0
    """
    new_matrix = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    length = 0

    """Checks if the matrix is a list"""
    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)
        if type(i) is not int and type(i) is not float:
            raise TypeError(message)
    for row in matrix[1:]:
        if len(row) != len(matrix[0])
        raise TypeError("Each row of the matrix must have the same size")

    """Checking if div is a number(integer/float)
    and equal to 0"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """All elements of the matrix divided by div
    and rounded to 2 decimal places"""
    for num in matrix:
        division = [round(i / div, 2) for i in num]
        new_matrix.append(divison)

    return new_matrix
