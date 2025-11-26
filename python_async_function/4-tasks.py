#!/usr/bin/env python3
"""Module providing task_wait_n, an async function that launches
multiple task_wait_random coroutines and returns their delays sorted."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return the list of delays
    in ascending order.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: A sorted list containing all the delays.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Run them concurrently and gather results
    delays = await asyncio.gather(*tasks)

    # Return the delays sorted
    return sorted(delays)
