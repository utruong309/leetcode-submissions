class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Input: 
        - n cities labeled 0 - n - 1 
        - 0 -> 1 -> 2 -> ... -> n - 1 
        - queries[i] = [ui, vi] adds another path from ui to vi 
        Output: 
        - answer[i] = shortest path from 0 -> n - 1 after queries[i] 
        Approach: 
        - unweighted graph -> BFS 
        - update edges for each of the query -> call BFS helper to find shortest path from 0 -> n - 1 
        """
        adj = defaultdict(list)

        # initial graph
        for i in range(n - 1): 
            adj[i].append(i + 1)
        
        def bfs(graph, seen): 

            queue = deque() 
            queue.append((0, 0))
            seen.add(0)

            while queue: 
                current, dist = queue.popleft() 

                if current == n - 1: 
                    return dist

                seen.add(current)

                for nei in graph[current]: 
                    if nei not in seen: 
                        seen.add(nei)
                        queue.append((nei, dist + 1))
        
        ans = [] 

        for a, b in queries: 
            adj[a].append(b)

            ans.append(bfs(adj, set()))
        
        return ans