#!/usr/bin/env python3
"""LRU CACHING"""


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        assign to dict self.cache_data the item value
        key for the key 'key'
        if no of items in the dict is higher than
        than that of Basecaching.MAX_ITEMS
        discard last recently used
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.queue.popleft()
                del self.cache_data[popped]
                print("DISCARD: " + str(popped))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key, None)
