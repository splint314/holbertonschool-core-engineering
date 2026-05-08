#!/usr/bin/env python3

def update_dictionary(d, key, value):

    """Replaces or adds key/value in a dictionary.

    Args:
    d (dict): The dictionary to update.
    key: The key to replace or add.
    value: The value associated with the key.

    Returns:
    The updated dictionary.
    """

    d[key] = value
    return d

    if __name__ == "__main__":

        my_dict = {'a': 1, 'b': 2}
    print(update_dictionary(my_dict, 'b', 3))
    print(update_dictionary(my_dict, 'c', 4))
