#!/usr/bin/python3
'''function that returns a list of integers
representing the Pascal's triangle of n'''


def pascal_triangle(n):
    '''pascal_triangle function'''
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) is not n:
        triangle = triangles[-1]
        temp = [1]
        for x in range(len(triangle) - 1):
            temp.append(triangle[x] + triangle[x + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
