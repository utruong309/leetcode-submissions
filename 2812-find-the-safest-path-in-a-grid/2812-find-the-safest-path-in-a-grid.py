class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque() 
        visited = set() 
        minDist = {} 

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    queue.append((i, j, 0))
                    visited.add((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue: 
            size = len(queue)

            for _ in range(size): 
                r, c, dist = queue.popleft() 
                minDist[(r, c)] = dist

                for x, y in directions: 
                    next_r, next_c = r + x, c + y 

                    if 0 <= next_r < rows and 0 <= next_c < cols and (next_r, next_c) not in visited: 
                        visited.add((next_r, next_c))
                        queue.append((next_r, next_c, dist + 1))
        
        max_heap = [(-minDist[(0, 0)], 0, 0)]   
        seen = {(0, 0)}

        while max_heap: 
            cost, r, c = heapq.heappop(max_heap)
            cost = -cost

            if r == rows - 1 and c == cols - 1:
                return cost 

            for x, y in directions: 
                next_r, next_c = r + x, c + y

                if 0 <= next_r < rows and 0 <= next_c < cols and (next_r, next_c) not in seen: 
                    new_cost = min(cost, minDist[(next_r, next_c)])
                    seen.add((next_r, next_c))
                    heapq.heappush(max_heap, (-new_cost, next_r, next_c))
        
        return 0