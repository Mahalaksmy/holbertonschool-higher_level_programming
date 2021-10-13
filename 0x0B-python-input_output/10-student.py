#!/usr/bin/python3
"""Creation of the
a class Student that defines a student """


class Student:

    def __init__(self, first_name, last_name, age):
        """Instantion of the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method thar retrieves a dictionary """

        if attrs is not None:
            listx = {}
            for i in attrs:
                if i in self.__dict__:
                    listx[i] = self.__dict__[i]
            return listx
        return self.__dict__
