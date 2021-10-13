#!/usr/bin/python3
"""Write a function that writes an Object
to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """ This a function that writes an Object
    to a text file"""

    with open(filename, 'w') as filen:
        filen.write(json.dumps(my_obj))
