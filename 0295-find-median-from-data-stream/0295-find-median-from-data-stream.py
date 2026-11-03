class MedianFinder:

    def __init__(self):
        self.min_heap = [] 
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # the extra element will be in the left half 
        if len(self.min_heap) > len(self.max_heap): 
            elem = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -elem)
        
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap): 
            first = self.min_heap[0]
            sec = -self.max_heap[0]
            return (first + sec) / 2 
        
        return -self.max_heap[0]

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()