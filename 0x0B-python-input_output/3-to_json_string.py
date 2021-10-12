#!/usr/bin/python3
"""Creation of the function that
returns the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """ Returns the JSON"""

    return json.dumps(my_obj)
