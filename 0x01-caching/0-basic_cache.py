#!/usr/bin/env python3
"""
    0-basic_cache mod
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        basic caching system class
    """
    def put(self, key, item):
        """
            insertion of keys and items to caching system
        """
        if not key or not item:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
            gets the item of a key in the caching system
        """
        if not key or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
