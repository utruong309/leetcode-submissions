class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        minDist = {} 

        for u, v, w in times: 
            adj[u].append((v, w))
        
        queue = [] # min heap 
        heapq.heappush(queue, (0, k)) 
        cnt = 0 

        while queue: 
            w, node = heapq.heappop(queue)

            if node in minDist and w >= minDist[node]: 
                continue 

            minDist[node] = w 
            cnt += 1 

            if cnt == n: 
                return w

            for nei, weight in adj[node]: 
                if nei not in minDist: 
                    heapq.heappush(queue, (w + weight, nei))
        
        return -1