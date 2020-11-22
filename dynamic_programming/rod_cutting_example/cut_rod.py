"""
Dynamic programming example:

The rod-cutting problem is the following. Given a rod of length n inches and a table of prices p_i for i=1,2,...n,
determine the maximum revenue r_n obtainable by cutting up the rod and selling the pieces. Note that if the price p_n
for a rod of length n is large enough, an optimal solution may require no cutting at all.

@author: Duncan Mazza
"""


import numpy as np
from dynamic_programming.rod_cutting_example.rod_value_lookup import *


def max_value_recurse(rod_len: int) -> float:
    """
    Return the maximum value of a rod using a recursive top-down approach
    :param rod_len: Length of the rod
    :return: Maximum value obtainable from the rod
    """
    if rod_len == 0:
        return 0
    max_val = 0.0
    for i in range(1, rod_len + 1):
        max_val = max(max_val, RodValueLookup.get_val(i) + max_value_recurse(rod_len - i))
    return max_val


def max_value_bottom_up(rod_len: int) -> float:
    """
    Return the maximum value of a rod using a bottom-up approach
    :param rod_len: Length of the rod
    :return: Maximum value obtainable from the rod
    """
    saved = np.zeros(shape=(rod_len + 1,), dtype=np.float)
    for j in range(1, rod_len + 1):
        max_val = 0.0
        for i in range(1, j + 1):
            max_val = max(max_val, RodValueLookup.get_val(i) + saved[j - i])
        saved[j] = max_val
    return saved[rod_len]


if __name__ == "__main__":
    rod_len = 3

    print("Maximum value from rod of length {}: {}".format(rod_len, max_value_recurse(rod_len)))

