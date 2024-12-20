#!/usr/bin/env python3
""" Write a function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing a
start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination
parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


import csv
import math
from typing import Tuple, List, Dict
from itertools import islice


def index_range(page: int, page_size) -> Tuple:
    """The function should return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters.
    """

    # formulae for start is page which is 1 - 1 * page_size
    # end is start + page_size (0 + 12) = 12
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
            return self.dataset()

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page that takes two integer arguments page with default
        value 1 and page_size with default value 10.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        # sliced_result = data[start:end] if data else []
        sliced_result = list(islice(data, start, end))

        return sliced_result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """"
        Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation.

        You can use the math module if necessary.
        """
        page_data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": max(1, page - 1) if page > 1 else None,
            "total_pages": total_pages
        }
