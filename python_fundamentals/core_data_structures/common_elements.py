#!/usr/bin/env python3

def common_elements(set_1, set_2):

    """Returns a set of common elements in two sets."""

    return set_1.intersection(set_2)


if __name__ == "__main__":

    set_1 = {1, 2, 3, 4}
    set_2 = {3, 4, 5, 6}
    print(common_elements(set_1, set_2))
