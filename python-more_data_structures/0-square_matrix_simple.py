#!/usr/bin/python3
"""Module that provides a function to square matrix values.

Functions
---------
square_matrix_simple(matrix=[])
	Returns a new matrix with each value squared.
"""


def square_matrix_simple(matrix=[]):
	"""Compute the square of all integers in a 2D matrix.

	Args:
		matrix (list of lists of int): 2D list of integers.

	Returns:
		list of lists of int: New 2D list where each value is squared.

	The original matrix is not modified.
	"""
	# Use list comprehensions (or map) to build a new matrix so the
	# original is not modified. An empty matrix returns an empty list.
	return [list(map(lambda x: x * x, row)) for row in matrix]

