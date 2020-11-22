"""
Tests for the rod-cutting example.

@author: Duncan Mazza
"""

import pytest
from dynamic_programming.rod_cutting_example.cut_rod import *
from typing import Dict, List


cut_rod_test_args: List[List[int, float]] = \
    [[0, 0.0],
     [1, 2.0],
     [2, 4.0],
     [3, 6.0],
     [4, 8.0]]


class RodValueLookup:
    """
    Provides functionality for looking up the value of a rod of arbitrary length.

    :cvar _lookup_dict: Key: length of a rod; value: value of the rod
    :cvar _default_val: Default value of a rod if its length is not in the lookup dictionary
    """
    _lookup_dict : Dict[int, float] = {1: 2.0, 2: 4.0, 3: 6.0, 4: 7.0, 5: 8.0, 6: 8.0, 7: 8.0, 9: 9.0}
    _default_val : float = 10.0

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


@pytest.mark.parametrize("cut_rod_test_arg", cut_rod_test_args)
def test_max_value_recursive(cut_rod_test_arg):
    assert max_value_recurse(cut_rod_test_arg[0]) == cut_rod_test_arg[1]


@pytest.mark.parametrize("cut_rod_test_arg", cut_rod_test_args)
def test_max_value_bottom_up(cut_rod_test_arg):
    assert max_value_bottom_up(cut_rod_test_arg[0]) == cut_rod_test_arg[1]
