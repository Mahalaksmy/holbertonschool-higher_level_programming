#!/usr/bin/python3
"""New Class Square"""


class Square:
    """ Aclass Square that defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0):
        """Initialize square with the size"""
        self.__size = size

        """ Exception with the message"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
