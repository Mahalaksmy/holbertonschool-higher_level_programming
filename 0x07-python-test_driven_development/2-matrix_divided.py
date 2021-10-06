#!/usr/bin/python3
"""Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    div all elements of a matrix
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix" +
                        "(list of lists) of integers/floats")

    len_rows = []

    for row in matrix:
        len_rows.append(len(row))
    if not all(elements == len_rows[0] for elements in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]

    return new_matrix
