#!/usr/bin/python3
"""New class rectangle """


class Rectangle:
    """New class rectangle that defines a rectangle:"""

    def __init__(self, width=0, height=0):
        """Initialize square with the size width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """property  to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """New value for width"""

        """ Exception with the message"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__widget = value

    @property
    def height(self):
        """property  to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """New value for width"""

        """ Exception with the message"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__height = value
