#!/usr/bin/python3
"""Creation of the function
that returns an object
(Python data structure) represented by a JSON string"""

import json


def from_json_string(my_str):
    """ Returns the an Object"""

    return json.loads(my_str)
