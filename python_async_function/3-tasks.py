#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that executes wait_random
    with the specified max_delay.

    Args:
        max_delay (int): maximum delay for wait_random

    Returns:
        asyncio.Task: a running asynchronous task
    """

    return asyncio.create_task(wait_random(max_delay))
