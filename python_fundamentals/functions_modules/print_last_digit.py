#!/usr/bin/env python3

def print_last_digit(number):
    """Print the last digit of a number.

    Args:
        number (int): The number to extract the last digit from.

    Returns:
        int: The last digit of the number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
