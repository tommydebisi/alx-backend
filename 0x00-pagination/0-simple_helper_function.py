#!/usr/bin/env python3
"""
    0-simple_helper_function mod
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        returns a tuple of start and end index corresponding to the range
        of indexes to return in a list for the given pagination parameters

        Args:
            page: page to read from
            page_size: number of rows to read from
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
