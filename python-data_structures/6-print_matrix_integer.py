#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Each row is printed on its own line with integers separated by
    a single space. Uses str.format() for integer formatting.
    """
    for row in matrix:
        print(' '.join("{:d}".format(i) for i in row))
