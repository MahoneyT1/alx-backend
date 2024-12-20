#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the
parent class BaseCaching
You can overload def __init__(self): but don’t forget to
call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item
value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following
by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from typing import Dict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching and is a
    caching system
    """
    def __init__(self):
        """calls the parents initializer and methods"""
        super().__init__()

    def put(self, key: str, item: Dict):
        """assign to the dictionary self.cache_data the item
        value for the key key.

        If key or item is None, this method should not do
        anything.
        """

        if key is not None and item is not None:
            # if cache_data is full remove the last inserted element
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD:{last_key}")

            self.cache_data[key] = item

    def get(self, key) -> Dict:
        """ Must return the value in self.cache_data
        linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """

        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
