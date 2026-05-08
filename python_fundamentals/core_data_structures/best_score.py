#!/usr/bin/env python3

def best_score(a_dictionary):

    """Returns a key with the biggest integer value.

    Args:
    a_dictionary (dict): The dictionary to search through.

    Returns:
    The key with the biggest integer value, or None if the dictionary is empty.
    """

    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key


if __name__ == "__main__":

    scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    print(best_score(scores))
