class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        """
        Input: 
        - unrooted weighted tree: n vertices, 0 -> n - 1 
        - edges[i] = [ai, bi, weighti]
        - signalSpeed 
        - a and b are connectable thru c if: 
            - a < b, a != c, b != c 
            - dist from c -> a is divisible by signalSpeed
            - dist from c -> b is divisible by signalSpeed
        Output: 
        count[i] = # of server pairs that are connectable thru server i

        Approach:
        - graph: {node: [list of nodes starting from it + weight]} 
        - dfs starting from each neighbor in that graph -> accumulate weight 
        - for a middle node c: 
            - cnt = # of nodes in each branch from c <=> dist[node] % signalSpeed = 0 
            - count the current # of nodes alr visited 
            - new branch's # of nodes will pair with those -> multiply 
            - update # of nodes visited 
            - next time multiply next branch with those and update again 
        """
        adj = defaultdict(list)

        for a, b, w in edges: 
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        def dfs(node, weight, seen): # call dfs on each branch from current middle node
            seen.add(node)
            cnt = 0 

            if weight % signalSpeed == 0: 
                cnt += 1
            
            for nei, w in adj[node]: 
                if nei not in seen: 
                    cnt += dfs(nei, weight + w, seen)
            
            return cnt 

        n = len(edges) + 1 
        ans = [0] * n 

        for i in range(n): 
            pairs = 0 
            current_cnt = 0 
            visited = {i}

            for nei, w in adj[i]:  
                temp = dfs(nei, w, visited)
                pairs += temp * current_cnt
                current_cnt += temp
            
            ans[i] = pairs 
        
        return ans 