#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            if between two queries, certain rows are removed from the dataset,
            the user does not miss items from dataset when changing page
        """
        self.indexed_dataset()
        len_data = len(self.__indexed_dataset)
        assert type(index) == int and type(page_size) == int
        assert index < len_data

        data_list = []
        iter, count, next_ind = index, 0, None

        while True:
            if self.__indexed_dataset.get(iter):
                data_list.append(self.__indexed_dataset[iter])
                count += 1

            if count == page_size:
                # check if next_ind is not the total length of data
                next_ind = iter + 1 if iter + 1 != len_data else None
                break

            if iter == len(self.__indexed_dataset):
                break
            iter += 1

        return {
            'index': index,
            'data': data_list,
            'page_size': page_size,
            'next_index': next_ind
        }
