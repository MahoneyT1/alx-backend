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
from typing import Tuple, List
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
