#!/usr/bin/env python3
"""
    2-hypermedia_pagination mod
"""
import csv
import math
from typing import List, Tuple, Dict


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
            returns the appropriate page of the dataset correctly or
            empty list if out of range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        list_data = self.dataset()

        data_len = len(list_data)
        # check if start index can be accessed
        if start >= data_len:
            return []

        if end >= data_len:
            end = end - (end - data_len)

        return list_data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            takes page and page_size and returns a dictionary containing the
            following key-value pairs: page_size, page, data, next_page,
            prev_page, total pages
        """
        data = self.get_page(page, page_size)
        len_data = len(self.__dataset)
        prev_page = None if page == 1 else page - 1
        total_pages = len_data // page_size
        start, end = index_range(page, page_size)

        if end >= len_data:
            next_page = None
        else:
            next_page = page + 1

        if len_data % page_size != 0:
            total_pages += 1

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
