#!/usr/bin/env python3

"""Module that contains the read_file function"""


def read_file(filename: str) -> None:
    """Reads a text file and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
