#!/usr/bin/python3
"""Creation a function that
creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """ This a function  that creates
    an Object from a “JSON file"""

    with open(filename, 'r') as filen:
        return json.load(filen)
