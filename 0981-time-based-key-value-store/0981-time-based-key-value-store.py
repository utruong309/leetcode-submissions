class TimeMap:

    def __init__(self):
        """
        max heap: (timestamp, key, value)
        """
        self.max_heap = []  

    def set(self, key: str, value: str, timestamp: int) -> None: 
        heapq.heappush(self.max_heap, (-timestamp, key, value))

    def get(self, key: str, timestamp: int) -> str:
        
        current = self.max_heap.copy()

        while current and -current[0][0] > timestamp: 
            heapq.heappop(current)

        while current and current[0][1] != key: 
            heapq.heappop(current)
        
        if current: 
            return current[0][2]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)