#!/usr/bin/python3
"""LIFOCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key
        Discard last item if self.cache_data id higher than
        BaseCaching.MAX_ITEMS
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) <= self.MAX_ITEMS:
                pass
            else:
                del self.cache_data[self.last_key]
                print(f'DISCARD: {self.last_key}')
            self.last_key = key

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key:
            return self.cache_data.get(key, None)
