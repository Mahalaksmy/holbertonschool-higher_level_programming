#!/usr/bin/python3
"""Creation a function that returns True
if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """Function tha returns True or False"""

    return isinstance(obj, a_class)
