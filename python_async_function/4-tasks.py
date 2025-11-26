#!/usr/bin/env python3
"""
Run task_wait_random multiple times concurrently and return
all resulting delays in ascending order (without using sort()).
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random n times concurrently.
    Collect each delay and return them in ascending order.
    """
    # Create all tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    # Process tasks as they finish
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task

        # Insert delay in ascending order
        for index, existing in enumerate(delays):
            if delay < existing:
                delays.insert(index, delay)
                break
        else:
            # If no earlier spot found → append at end
            delays.append(delay)

    return delays
