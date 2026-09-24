#!/usr/bin/python3
"""Build Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle with n rows."""
    if n <= 0:
        return []

    triangle = []
    for row_number in range(n):
        row = [1] * (row_number + 1)
        for index in range(1, row_number):
            row[index] = (triangle[row_number - 1][index - 1]
                          + triangle[row_number - 1][index])
        triangle.append(row)
    return triangle