class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # dict of key -> Node
        self.left_dummy_node = Node(0,0)
        self.right_dummy_node = Node(0,0)
        self.left_dummy_node.next = self.right_dummy_node
        self.right_dummy_node.prev = self.left_dummy_node


    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_node(self, node):
        prev_node = self.right_dummy_node.prev
        next_node = self.right_dummy_node
        node.next = next_node
        node.prev = prev_node
        prev_node.next = node
        next_node.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        if len(self.cache) > self.capacity:
            lru_node = self.left_dummy_node.next
            self.remove_node(lru_node)
            del self.cache[lru_node.key]