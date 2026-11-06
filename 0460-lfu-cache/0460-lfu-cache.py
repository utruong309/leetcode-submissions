class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.heap = [] # (freq, time, key)
        self.cache = {} # key -> val 
        self.time = {} # key -> time 
        self.freq = defaultdict(int) # key -> freq 
        self.timestamp = 0 

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1 
        
        self.time[key] = self.timestamp
        self.timestamp += 1 
        self.freq[key] += 1 
        heapq.heappush(self.heap, (self.freq[key], self.time[key], key))
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:  
            if len(self.cache) == self.capacity: 
                while self.heap and self.heap[0][1] != self.time[self.heap[0][2]]:
                    heapq.heappop(self.heap)
                
                lfu =  heapq.heappop(self.heap)[2]
                del self.time[lfu]
                del self.cache[lfu]
                del self.freq[lfu]

        self.time[key] = self.timestamp
        self.timestamp += 1 
        self.freq[key] += 1 
        self.cache[key] = value 
        heapq.heappush(self.heap, (self.freq[key], self.time[key], key))

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)