#!/usr/bin/env python3
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of running wait_n(n, max_delay).
    Return the average time per coroutine.

    Args:
        n (int): number of coroutines to run
        max_delay (int): maximum delay passed to wait_n

    Returns:
        float: the average runtime per coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
