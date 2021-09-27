#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    var = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            var += 1
        print("")
        return var
    except:
        print("")
        return var
