class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Input: 
        - equations[i] = [ai, bi] -> ai / bi -> values[i] is ans to that 
        - queries[j] = [cj, dj] -> cj / dj = ? 
        Output: 
        - answer[j] = ans to queries[j]
        Approach: 
        - a / b * b / c = a / c 
        - graph: {a: [(b, 2,0)], b: [(c, 3.0)]}
        - dfs(source, target, amount)
            - multiply value of source / target each call 
            - stop when source = target
        """
        adj = defaultdict(list)

        for i, entry in enumerate(equations): 
            a, b = entry
            value = values[i]
            adj[a].append((b, value))
            adj[b].append((a, 1 / value))
        
        # print(adj)
        
        def dfs(source, target, amount, visited): 
            if source == target: 
                return amount 
            
            visited.add(source)
            
            for nxt, amt in adj[source]:
                if nxt not in visited: 
                    res = dfs(nxt, target, amount * amt, visited) 
                    if res != -1: 
                        return res 
            
            return -1 
        
        ans = [] 

        for a, b in queries: 
            if a not in adj or b not in adj: 
                ans.append(-1)
            else: 
                ans.append(dfs(a, b, 1, set()))
        
        return ans