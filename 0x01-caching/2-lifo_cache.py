#!/usr/bin/env python3
"""
    2-lifo_cache mod
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        implemention of Last In First Out cache
        replacement policy
    """
    def __init__(self):
        """ constructor function """
        self.__cache_checker = []
        self.__counter = BaseCaching.MAX_ITEMS - 1
        self.__repeat = 0
        super().__init__()

    def put(self, key, item):
        """
            sets given key to item in the caching system
        """
        if key is None or item is None:
            return

        if len(self.cache_data) != BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.__cache_checker.append(key)
        else:
            if self.cache_data.get(key):
                self.__repeat = 1
                return

            discarded = self.__cache_checker.pop(self.__counter)
            del self.cache_data[discarded]
            print("DISCARD: {}".format(discarded))

            self.cache_data[key] = item
            self.__cache_checker.append(key)
            self.__counter -= 1

            if self.__counter == -1 or self.__repeat:  # reset count
                self.__counter = BaseCaching.MAX_ITEMS - 1
                self.__repeat = 0

    def get(self, key):
        """ gets the value at the given key in the caching sytem """
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
