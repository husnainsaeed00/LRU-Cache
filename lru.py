class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.cache = {}  # Dictionary to store key-node mappings
        self.head = Node(-1, -1)  # Dummy head node
        self.tail = Node(-1, -1)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _deleteNode(self, node):
        # Remove a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addNode(self, node):
        # Add a node to the front of the linked list
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._deleteNode(node)
        self._addNode(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._deleteNode(node)
            node.val = value
            self._addNode(node)
        else:
            if len(self.cache) == self.size:
                # Remove the least recently used node (tail.prev)
                del self.cache[self.tail.prev.key]
                self._deleteNode(self.tail.prev)

            # Create a new node and add it to the front of the list
            node = Node(key, value)
            self.cache[key] = node
            self._addNode(node)
