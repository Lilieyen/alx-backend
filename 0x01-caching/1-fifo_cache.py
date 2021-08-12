#!/usr/bin/python3
"""class FIFOCache that inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data.keys()) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.queue.append(key)
            else:
                self.cache_data[key] = item
                discard = self.queue[0]
                del self.cache_data[self.queue[0]], self.queue[0]
                self.queue.append(key)
                print(f'DISCARD: {discard}')

    def get(self, key):
        """
        must return value in self.cache_data linked to key
        """
        if key:
            return self.cache_data.get(key, None)
