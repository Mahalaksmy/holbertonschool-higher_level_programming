#!/usr/bin/python3
"""This class will be the base
of all other classes in this project"""

import os.path
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """This a method that returns
        the JSON string (list_dictionaries)"""

        if list_dictionaries is None:
            list_dictionaries = []

        list_dictionaries = json.dumps(list_dictionaries)
        return str(list_dictionaries)
        
        
