#!/usr/bin/python3
""" a class Square that inherits
from Rectangle (9-rectangle.py):"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """Instantiation with size"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of rhe Square"""

        return self.__size ** 2
