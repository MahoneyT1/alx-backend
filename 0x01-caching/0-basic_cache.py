#!/usr/bin/env python3
""" Create a class BasicCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """iherites BaseCaching caching system"""
    def __init__(self):
        """calls the parents class"""
        super().__init__()

    def put(self, key, item):
        """inserts a record in the cache using a key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns a cache by the key"""
        return self.cache_data.get(key) if key \
            in self.cache_data.keys() else None
