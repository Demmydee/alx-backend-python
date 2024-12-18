#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax
A function that takes an integer max_delay and return a asyncio.Task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Take an integer max_delay and return a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
