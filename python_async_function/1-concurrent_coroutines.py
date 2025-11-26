#!/usr/bin/env python3
"""
Run wait_random multiple times concurrently and return
all resulting delays in ascending order (without using sort()).
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times concurrently.
    Collect every delay and return them in ascending order.
    """
    # Create all tasks up front
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays: List[float] = []

    # Process tasks as they complete
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task

        # Insert delay into the list in ascending order
        for index, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(index, delay)
                break
        else:
            # No break → append at the end
            delays.append(delay)

    return delays
