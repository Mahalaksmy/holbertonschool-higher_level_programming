#!/usr/bin/python3
""" This is a module containing a function
that returns the addition of 2 integers.
"""


def add_integer(a, b=98):
    """ function that returns the addition of 2 integers.
        Value: a and b must be integers or floats
        Returns an integer: the addition of a and b
    """
# validations for parameter a
    if a is None:
        a = 0

    if type(a) is float:
        a = int(a)

    if type(a) is not int:
        raise TypeError("a must be an integer")

# validations for parameter a
    if type(b) is float:
        b = int(b)

    if type(b) is not int:
        raise TypeError("b must be an integer")

# Return the addition of a and b
    return(a + b)
