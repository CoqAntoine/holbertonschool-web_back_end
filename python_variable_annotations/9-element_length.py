#!/usr/bin/env python3
"""
This module provides a function that returns the length
of each element in a list of sequences.
"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains a
    sequence from lst and its corresponding length.
    """
    return [(element, len(element)) for element in lst]
