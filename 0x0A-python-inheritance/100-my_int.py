#!/usr/bin/python3
"""creation a class MyInt that inherits from int"""


class MyInt(int):
    """This a class Myint"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
