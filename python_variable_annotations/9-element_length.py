#!/usr/bin/env python3
"""
This module provides a function that returns the length
of each element in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains a
    sequence from lst and its corresponding length.
    """
    return [(i, len(i)) for i in lst]