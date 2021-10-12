#!/usr/bin/python3
""" Creation of the function
that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """This is a function that reads
    and prints files"""

    with open(filename, encoding="utf8") as filen:
        for line in filen:
            print(line, end="")
