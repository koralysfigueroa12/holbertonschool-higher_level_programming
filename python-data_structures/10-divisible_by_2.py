#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False whether each element is a multiple of 2.

    The returned list has the same size as the input list.
    """
    return [i % 2 == 0 for i in my_list]
