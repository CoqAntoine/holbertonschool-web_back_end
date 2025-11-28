#!/usr/bin/env python3
"""A coroutine called measure_runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension 4 times in parallel and measure total runtime.

    Returns:
        float: Total execution time in seconds.
    """
    start = time.time()

    # launch 4 async comprehensions concurrently
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end = time.time()
    return end - start
