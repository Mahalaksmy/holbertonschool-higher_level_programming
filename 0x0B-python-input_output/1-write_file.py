#!/usr/bin/python3
""" Creation of the function
Write a function that writes
a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """This is a function that write
    a string to a tex file"""

    with open(filename, 'w+', encoding="utf8") as filen:
        f = filen.write(text)
        return f
