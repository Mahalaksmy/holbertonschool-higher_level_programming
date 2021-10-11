#!/usr/bin/python3
"""Creation of the  a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """ This a class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
