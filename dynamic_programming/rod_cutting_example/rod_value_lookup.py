"""
Helper code for the Dynamic programming rod-cutting example that provides the capability for looking up the value of a
piece of rod of a  given length.

@author: Duncan Mazza
"""

from typing import Dict, List


class RodValueLookup:
    """
    Provides functionality for looking up the value of a rod of arbitrary length.

    :cvar _lookup_dict: Key: length of a rod; value: value of the rod
    :cvar _default_val: Default value of a rod if its length is not in the lookup dictionary
    :cvar cut_rod_test_args: List of parameters used for testing the max value calculation
    """
    _lookup_dict : Dict[int, float] = {1: 2.0, 2: 4.0, 3: 6.0, 4: 7.0, 5: 8.0, 6: 8.0, 7: 8.0, 9: 9.0}
    _default_val : float = 10.0
    cut_rod_test_args: List[List] = \
        [[0, 0.0],
         [1, 2.0],
         [2, 4.0],
         [3, 6.0],
         [4, 8.0]]

    @staticmethod
    def get_val(length: int) -> float:
        """
        :param length: length of the rod
        :return: value of the rod
        """
        if length == 0:
            return 0
        elif length < 0:
            raise ValueError("length cannot be <0")
        elif RodValueLookup._lookup_dict.__contains__(length):
            return RodValueLookup._lookup_dict[length]
        else:
            return RodValueLookup._default_val
