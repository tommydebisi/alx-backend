#!/usr/bin/env python3
"""
    1-simple_pagination mod
"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            takes in parameters and returns the items in that range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        list_data = self.dataset()

        data_len = len(list_data)
        # check if start index can be accessed
        if start >= data_len:
            return []

        # adjust end index if more the length of dataset
        if end >= data_len:
            end = data_len

        return list_data[start: end]
