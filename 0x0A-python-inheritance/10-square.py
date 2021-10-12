#!/usr/bin/python3
""" Creation a class Square that inherits
from Rectangle (9-rectangle.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class of the square
    Private instance with  attribute size"""

    def __init__(self, size):
        """Initializes a Square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string"""

        return super().__str__()

    def area(self):
        """Area of the Square instance
        """

        return self.__size ** 2
