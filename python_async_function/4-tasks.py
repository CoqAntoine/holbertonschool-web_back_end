#!/usr/bin/env python3
"""
This module provides a function that runs several asynchronous
tasks created with task_wait_random and returns their delays
in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the given max_delay.
    Return the list of delays in ascending order, without using sort().

    Args:
        n (int): number of tasks to create
        max_delay (int): maximum delay passed to task_wait_random

    Returns:
        List[float]: delays from all tasks, sorted in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task

        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break

        if not inserted:
            delays.append(delay)

    return delays
