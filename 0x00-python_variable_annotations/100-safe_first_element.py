#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return first element if there is a sequence, otherwise return None
    """
    if lst:
        return lst[0]
    else:
        return None
