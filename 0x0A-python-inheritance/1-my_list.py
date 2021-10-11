#!/usr/bin/python3
""" Creation of a class MyList
that inherits from list"""


class MyList(list):
    """This a class MyList that inherits from list"""

    def print_sorted(self):
        new_list = sorted(self[:])
        print("{}".format(new_list))
