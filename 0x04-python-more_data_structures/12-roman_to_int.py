#!/usr/bin/python
def roman_to_int(roman_string):
    x = 0
    num_romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string == 0:
        return 0

    for i in roman_string:
        if i in roman_string:
            nget = num_romans.get(i)
            x = x + nget
    return(x)
