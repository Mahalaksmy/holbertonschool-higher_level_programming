#!/usr/bin/python3
"""Creation a function that
returns a list of list of integers
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Function the Pascal’s triangle of n"""

    if n <= 0:
        return []

    pascal_triangle = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if(j < i):
                if(j == 0):
                    pascal_triangle[i].append(1)
                else:
                    pascal_triangle[i].append(pascal_triangle[i-1]
                                              [j] + pascal_triangle[i-1][j-1])
            elif(j == i):
                pascal_triangle[i].append(1)
    return pascal_triangle
