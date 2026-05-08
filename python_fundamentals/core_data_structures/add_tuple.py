#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):

    """Adds two tuples element-wise.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A new tuple containing the element-wise sum of the input tuples.
    """
    # Ensure both tuples have at least 2 elements by padding with zeros
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a new tuple with the element-wise sum
    return (a[0] + b[0], a[1] + b[1])
