#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = 1
        for j in i:
            print("{:d}".format(j), end="")
            if len(i) > x:
                print(end=" ")
            x += 1
        print(end="\n")
