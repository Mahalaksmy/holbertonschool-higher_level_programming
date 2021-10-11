#!/usr/bin/python3
"""Creation of a class BaseGeometry."""


class BaseGeometry:
    """This is a class BaseGeometry"""

    def area(self):
        """Public instance method that raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value """

        if type(name) == str:

            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))

            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
