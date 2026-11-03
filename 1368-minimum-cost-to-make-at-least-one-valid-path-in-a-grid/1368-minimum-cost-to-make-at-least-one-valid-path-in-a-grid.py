class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mp = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        minCost = {}

        queue = [] # priority queue 
        queue.append((0, 0, 0))

        rows = len(grid)
        cols = len(grid[0])

        while queue: 
            cost, row, col = heapq.heappop(queue)
            sign = grid[row][col]

            if (row, col) in minCost and cost >= minCost[(row, col)]: 
                continue 

            minCost[(row, col)] = cost

            for x, y in directions: 
                next_r, next_c = row + x, col + y 

                if 0 <= next_r < rows and 0 <= next_c < cols: 
                    if mp[sign] == (x, y): 
                        current_cost = 0 
                    else: 
                        current_cost = 1 
                    
                    if (next_r, next_c) not in minCost or cost + current_cost < minCost[(next_r, next_c)]: 
                        heapq.heappush(queue, (cost + current_cost, next_r, next_c))
        
        return minCost[(rows - 1, cols - 1)]