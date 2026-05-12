#!/usr/bin/env python3

def size_validation(size):
    """Validate the size of the square."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
