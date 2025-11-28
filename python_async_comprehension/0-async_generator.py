#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """
    Asynchronously generate 10 random numbers.

    This coroutine loops 10 times, waiting asynchronously for
    1 second in each iteration, then yields a random float
    between 0 and 10.

    Yields:
        float: A random number in the range [0, 10).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
