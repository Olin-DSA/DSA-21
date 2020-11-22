"""
Tests for the rod-cutting example.

@author: Duncan Mazza
"""

import pytest
from dynamic_programming.rod_cutting_example.cut_rod import *
from dynamic_programming.rod_cutting_example.rod_value_lookup import RodValueLookup


@pytest.mark.parametrize("cut_rod_test_arg", RodValueLookup.cut_rod_test_args)
def test_max_value_recursive(cut_rod_test_arg):
    assert max_value_recurse(cut_rod_test_arg[0]) == cut_rod_test_arg[1]


@pytest.mark.parametrize("cut_rod_test_arg", RodValueLookup.cut_rod_test_args)
def test_max_value_bottom_up(cut_rod_test_arg):
    assert max_value_bottom_up(cut_rod_test_arg[0]) == cut_rod_test_arg[1]
