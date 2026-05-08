#!/usr/bin/env python3

def element_at(my_list, idx):
    """Returns the element at a specific position in a list.

    Args:
        my_list (list): The list to search through.
        idx (int): The index of the element to return.

    Returns:
    The element at the specified index, or None if the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
