class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """
        Input: 
        - directed graph 
        - n nodes
        - graph[i] = [neighbors of ith node]
        - ith node is terminal node if len(graph[i]) = 0 
        - a node is a safe node if every path starting from that node leads to a terminal node 
        Output: Array of all safe nodes 

        Topological sort
        - terminal nodes: no outgoing edges -> outdegree = 0 
        - outdegree[i]: # of outgoing edges of ith node 
        - reverse edge -> dict {node: [list of nodes that can reach it]}
            - decrement outdegree of nodes in that list if a node is safe to mark a path as safe 
            - if a node has no outgoing edges left -> safe -> can be pushed to queue 
        """
        n = len(graph)
        outdegree = [0] * n
        res = []  

        for i in range(n): 
            outdegree[i] = len(graph[i])
        
        reversed = defaultdict(list)

        for i, entry in enumerate(graph): 
            for nei in entry: 
                reversed[nei].append(i)
        
        queue = deque() 

        for i in range(n): 
            if outdegree[i] == 0:
                queue.append(i)
        
        while queue: 
            current = queue.popleft() 
            res.append(current)

            for nei in reversed[current]: 
                outdegree[nei] -= 1 
                if outdegree[nei] == 0: 
                    queue.append(nei)
        res.sort() 
        return res 