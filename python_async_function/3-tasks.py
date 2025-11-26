#!/usr/bin/env python3
"""Module for creating asyncio tasks from wait_random."""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that runs wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The created asynchronous task.
    """
    return asyncio.create_task(wait_random(max_delay))