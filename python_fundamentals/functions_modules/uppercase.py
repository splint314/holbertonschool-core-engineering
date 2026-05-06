#!/usr/bin/env python3

def uppercase(str):
    """function that prints a string in uppercase followed by a new line."""
    result = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    print("{}".format(result))
