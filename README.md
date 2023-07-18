# LRU Cache

LRU Cache is a data structure that follows the constraints of a Least Recently Used (LRU) cache. It provides the ability to store key-value pairs and perform efficient operations such as retrieving the value for a given key and updating or inserting key-value pairs. The LRU Cache has a fixed capacity and evicts the least recently used items when the capacity is exceeded.

This implementation of the LRU Cache provides the following methods:

- `LRUCache(capacity)`: Initializes a new LRU Cache with the given capacity.
- `get(key)`: Returns the value associated with the given key if it exists in the cache, otherwise returns -1.
- `put(key, value)`: Updates the value for the given key if it exists in the cache. If the key does not exist, it adds the key-value pair to the cache. If the capacity is exceeded, it evicts the least recently used key-value pair.

## Usage

```python
# Create an LRU Cache with capacity 2
cache = LRUCache(2)

# Insert key-value pairs into the cache
cache.put(1, 1)
cache.put(2, 2)

# Retrieve values from the cache
value1 = cache.get(1)  # Returns 1
value2 = cache.get(2)  # Returns 2
value3 = cache.get(3)  # Returns -1 (key does not exist)

# Update the value for an existing key
cache.put(1, 10)

# Eviction may occur when capacity is exceeded
cache.put(3, 3)  # Evicts key 2 (least recently used)

# Retrieve values again
value1 = cache.get(1)  # Returns 10
value2 = cache.get(2)  # Returns -1 (evicted)
value3 = cache.get(3)  # Returns 3
Time Complexity
The get and put operations of the LRUCache class each run in O(1) average time complexity, providing efficient access to the cache.

Space Complexity
The space complexity of the LRUCache class is O(capacity) as it requires additional space to store the key-value pairs and maintain the linked list structure.

