class Node: 
    def __init__(self, key, val): 
        self.key = key
        self.val = val 
        self.prev = None 
        self.next = None 

class LRUCache:
    """
    Create a node for each key-val pair
    - key
    - val
    - prev
    - next 
    - dummy nodes: 
        - left -> least recently used node 
        - right -> most recently used node 
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node 
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node): 
        prev_node = self.right.prev 
        prev_node.next = node
        node.prev = prev_node 
        node.next = self.right
        self.right.prev = node 
    
    def remove(self, node): 
        nxt_node = node.next 
        prev_node = node.prev 
        prev_node.next = nxt_node 
        nxt_node.prev = prev_node 

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1 
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: 
            lru = self.left.next 
            del self.cache[lru.key]
            self.remove(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)