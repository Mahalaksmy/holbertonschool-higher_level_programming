#!/usr/bin/python3
""" Creation of a a function that
inserts a line of text to a file,
after each line containing a
specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ This a a function that inserts
    a line of text to a file"""

    with open(filename, 'r') as filen:
        f = filen.readlines()

    with open(filename, 'w') as filen:
        string = ''
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        filen.write(string)
