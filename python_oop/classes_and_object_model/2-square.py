#!/usr/bin/env python3
"""Validate the size of the square."""


class Square:

    def __init__(self, size=0):
        """check if size is an integer."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """check if size is a positive integer."""
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
