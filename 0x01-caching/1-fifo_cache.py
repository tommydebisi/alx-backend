#!/usr/bin/env python3
"""
    1-fifo_cache mod
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        implementation of FIFO block replacement strategy
        class
    """
    def __init__(self):
        """ constructor function """
        self.__cache_checker = []
        super().__init__()

    def put(self, key, item):
        """ saves key with item in cache system """
        if key is None or item is None:
            return

        if len(self.cache_data) != BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.__cache_checker.append(key)
        else:
            # key is present no need for replacement
            if self.cache_data.get(key):
                return
            discarded = self.__cache_checker.pop(0)
            print("DISCARD: {}".format(discarded))
            del self.cache_data[discarded]

            self.cache_data[key] = item
            self.__cache_checker.append(key)

    def get(self, key):
        """ gets the value at the given key in the caching system """
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
