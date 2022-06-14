#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a
    start index and an end index corresponding to the
    range of indexes to return in a list
    for those particular pagination parameters.
    """
    end: int = page * page_size
    start: int = 0
    for i in range(page - 1):
        start += page_size
    return (start, end)
