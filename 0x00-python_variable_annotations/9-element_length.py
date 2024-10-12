#!/usr/bin/env python3
"""
Basic annotations - iterable object
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns values with appropriate types
    """
    return [(i, len(i)) for i in lst]
