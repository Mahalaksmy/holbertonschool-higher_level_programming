#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for x in my_list:
            if max < x:
                max = x
        return max
    return None
