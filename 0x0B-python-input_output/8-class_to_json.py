#!/usr/bin/python3
"""Creation a function that
returns the dictionary
description with simple data structure
for Json an object”"""


def class_to_json(obj):
    """ This a function  that returns
    the dictionary for Json"""

    return obj.__dict__
