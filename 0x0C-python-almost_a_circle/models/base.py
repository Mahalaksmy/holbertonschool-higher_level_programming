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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This a method that returns
        the JSON string (list_dictionaries)"""

        if list_dictionaries is None:
            list_dictionaries = []

        list_dictionaries = json.dumps(list_dictionaries)
        return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This a Method that writes the JSON
        string representation of list_objs"""

        newlist = []
        if list_objs is not None:
            for i in list_objs:
                newlist.append(cls.to_dictionary(i))

        with open('{}.json'.format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """This a method  that returns the list
        of the JSON string representation"""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
