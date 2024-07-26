#!/usr/bin/python3
"""
Prints a Pascal's triangle in a list
"""
def pascal_triangle(n):
    """
    Generates Pascal's triangle of n rows

    Args:
        n (int) - number of rows to generate

    Return:
        list - a list of lists representing a Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
