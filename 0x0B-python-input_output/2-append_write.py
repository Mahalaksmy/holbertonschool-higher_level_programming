#!/usr/bin/python3
""" Creation of the function
that appends a string
at the end of a text file (UTF8)
and returns the number of characters added:"""


def write_file(filename="", text=""):
    """This is a function that appends
    at the end of a text file"""

    with open(filename, 'a', encoding="utf8") as filen:
        f = filen.write(text)
        return f
