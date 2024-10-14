#!/usr/bin/env python3

"""
Import wait_random from the previous python file and write an async
routine called wait_n
It takes 2 int arguments (in this order) n and max_delay.
Spawn wait_random n times with the specified max_delay
wait_n should return the list of delays (float values) in ascending
order without using sort() because of concurrency
"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values)
    """
    list_delays = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(list_delays)
