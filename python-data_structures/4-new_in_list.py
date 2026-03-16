#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a copy of my_list with the element at idx replaced.

    If idx is negative or out of range, return a copy of the
    original list without modifying it.
    """
    new_list = my_list.copy()
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
