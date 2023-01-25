#!/usr/bin/env python3
"""
    100-lfu_cache mod
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        Implementation of the Least Frequently Used caching
        replacement policy
    """
    def __init__(self):
        """ constructor function """
        self.__cache_checker = []
        self.__cache_freq = []
        super().__init__()

    def put(self, key, item):
        """
            sets the given key to the item in the caching
            system
        """
        if key is None or item is None:
            return

        if len(self.cache_data) != BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.__cache_checker.append(key)
            self.__cache_freq.append(0)
        else:
            if self.cache_data.get(key):
                # increment frequency at key index in cache checker
                self.__cache_freq[self.__cache_checker.index(key)] += 1
                return

            min_freq = min(self.__cache_freq)
            list_min = [idx for idx, val in enumerate(
                        self.__cache_freq) if val == min_freq]
            if len(list_min) == BaseCaching.MAX_ITEMS:
                discarded = self.__cache_checker.pop(0)
                self.__cache_freq.pop(0)
            else:
                # if all not same freq, discard least recently used
                discarded = self.__cache_checker.pop(min(list_min))
                self.__cache_freq.pop(min(list_min))

            print("DISCARD: {}".format(discarded))
            del self.cache_data[discarded]

            self.cache_data[key] = item
            self.__cache_checker.append(key)
            self.__cache_freq.append(0)

    def get(self, key):
        """
            gets the item at the given key in the caching
            system
        """
        if key is None or not self.cache_data.get(key):
            return None

        # pop the same indexes in checker and freq
        key_idx = self.__cache_checker.index(key)
        self.__cache_checker.pop(key_idx)
        freq = self.__cache_freq.pop(key_idx)

        self.__cache_checker.append(key)
        # increment the frequency at the new key index
        self.__cache_freq.append(freq + 1)
        return self.cache_data.get(key)
