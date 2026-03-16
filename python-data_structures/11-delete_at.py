#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list.

    If idx is negative or out of range, the list is not modified.
    The deletion is performed in-place (no pop allowed).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
