#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Call task_wait_random
    """
    delay_time = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay_time)
