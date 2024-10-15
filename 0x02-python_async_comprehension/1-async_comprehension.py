#!/usr/bin/env python3
"""
Import async_generator from the previous task and write a coroutine
called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random
numbers.
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Collects 10 random numbers and returns 10 random numbers
    """
    return [rand async for rand in async_generator()]
