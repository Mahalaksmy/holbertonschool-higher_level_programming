#!/usr/bin/python3
""" This is a module function that prints
a square with the character #.
The value is size, must be an integer,
"""

def print_square(size):
    """ This is a function hat prints
    a square with the character #.
    """
    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print("")
    else:
        raise TypeError("size must be an integer")
