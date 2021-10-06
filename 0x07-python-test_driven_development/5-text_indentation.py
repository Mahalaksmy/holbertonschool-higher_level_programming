#!/usr/bin/python3
"""
This is a Module  that prints a text with 2
new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Pfunction that prints a text with 2
    new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    string = ""
    lines = 0

    for x in text:
        if not (lines == 0 and x == " "):
            string += x
            lines += 1
        if x in characters:
            string += '\n\n'
            lines = 0
    print(string, end="")
