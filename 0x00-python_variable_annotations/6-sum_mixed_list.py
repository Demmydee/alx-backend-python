#!/usr/bin/env python3
"""
Basic annotations - mixed list
"""
from typing import List, Union


def sum_mixed_list(mixed_lst: List[Union[int, float]]) -> float:
    """
    Returns sum of a list of integers and floats as a float
    """
    return float(sum(mixed_lst))
