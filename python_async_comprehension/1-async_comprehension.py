#!/usr/bin/env python3
"""A coroutine called async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from file using an async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [value async for value in async_generator()]
