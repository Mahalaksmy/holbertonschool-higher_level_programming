#!/usr/bin/python3
"""Creation of the
a class Student that defines a student """


class Student:

    def __init__(self, first_name, last_name, age):
        """Instantion of the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method thar retrieves a dictionary """
        return self.__dict__
