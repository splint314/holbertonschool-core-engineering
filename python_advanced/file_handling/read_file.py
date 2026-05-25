#!/usr/bin/env python3

"""Module that contains the read_file function"""

from fileinput import filename


def read_file(filename: str) -> None:

    """Reads a text file and prints it to stdout

    Args:
        filename (str): The name of the file to read
    """

    with open(filename, 'r') as f:
        print(f.read(), end='')

    if __name__ == "__main__":
        read_file("my_file_0.txt")
