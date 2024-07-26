#!/usr/bin/python3
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
        """
        loop creates the remaining n-1 rows
        start initializing the new row with 1
        """
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            """
            claculation of the middle elements of the new row
            to calculate addition of two numbers from above it is done
            """
            new_row.append(prev_row[j-1] + prev_row[j])

        """
        1 is added to the final row
        each row in Pascal's triangle ends with 1
        now the new row is added to the triangle
        """
        new_row.append(1)
        triangle.append(new_row)

    return triangle
