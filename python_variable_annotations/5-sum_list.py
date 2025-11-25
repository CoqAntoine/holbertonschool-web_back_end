#!/usr/bin/env python3
"""
This module provides a function that returns the sum of
all floating-point numbers in a list.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of all floats in the input_list.
    """
    return sum(input_list)
