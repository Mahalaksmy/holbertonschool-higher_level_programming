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
        """New value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting a new value for width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """property  to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """ New value for height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
