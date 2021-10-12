#!/usr/bin/python3
"""Creation  a function that adds a new attribute
to an object if it’s possible"""


def add_attribute(obj, att, val):
    """ this a function that adds
    a new attribute to an object if it’s possible"""

    if hasattr(obj, '__dict__') is True:
        setattr(obj, att, val)
    else:
        raise TypeError("can't add new attribute")
