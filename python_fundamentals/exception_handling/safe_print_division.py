#!/usr/bin/env python3

def safe_print_division(a, b):
	"""Divides 2 integers and prints the result.

	Args:
		a (int): The first integer.
		b (int): The second integer.

    Returns:
        The value of the division, otherwise None if the division can't be done.
    """
	result = None
	try:
		result = a / b
	except ZeroDivisionError:
		pass
	finally:
		print("Inside result: {}".format(result))
	return result
