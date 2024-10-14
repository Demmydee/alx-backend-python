#!/usr/bin/env python3
"""
Import wait_n from the previous file
Create a measure_time function with integers n and max_delay as arguments
The function measures the total execution time for wait_n(n, max_delay)
and returns total_time / n (float)
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Use time module to measure an appropriate elapsed time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return (total_time / n)
