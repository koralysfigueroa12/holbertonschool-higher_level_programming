#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line.

    Uses str.format() and does not cast integers to strings.
    """
    for i in my_list:
        print("{:d}".format(i))
