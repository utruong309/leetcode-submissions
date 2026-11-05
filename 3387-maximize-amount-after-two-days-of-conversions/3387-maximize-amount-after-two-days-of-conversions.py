class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        """
        Input: 
            - initialCurrency
            - pairs1[i] = [starti, targeti] -> convert from starti to targeti at rates1[i] on day 1
            - same for pairs2, rates2
            - target can be converted to start at 1 / rate 
            - want to convert initialCurrency to any other currencies so that it could be maximized at the end
        Output: Maximum amount of initialCurrency 
        
        1 EUR = 2 USD = 6 JPY
        1 USD  = 3 JPY 
        -> multipy rate when dfs 

        Approach: 
            - graph: {start: [(target, rate)], target: [(start, 1 / rate)]} -> bidirectional edge
            - calculate how much of each currency we can get after converting from initialCurrency 
                - the amount after day 1 is the initial unit -> multiply by that 
            - from those dfs on graph of day 2 to convert back to initialCurrency 
            - update maximum amount 
        """
        graph1 = defaultdict(list)

        for i, pair in enumerate(pairs1): 
            start, target = pair
            graph1[start].append((target, rates1[i]))
            graph1[target].append((start, 1 / rates1[i]))
        
        res = {initialCurrency: 1}

        def dfs(visited, graph, start, target, amount): 
            if start == target: 
                return amount 
            
            visited.add(start)

            for nxt, rate in graph[start]: 
                if nxt not in visited: 
                    ans = dfs(visited, graph, nxt, target, amount * rate)
                    if ans != -1: 
                        return ans
            
            return -1
        
        for key in graph1: 
            amt = dfs(set(), graph1, initialCurrency, key, 1)
            if amt != -1: 
                res[key] = amt 
        
        # print(res)

        graph2 = defaultdict(list)

        for i, pair in enumerate(pairs2): 
            start, target = pair
            graph2[start].append((target, rates2[i]))
            graph2[target].append((start, 1 / rates2[i]))
        
        maxAmt = float('-inf')

        for key in res: # starting currency for day 2 
            initial = res[key]
            amt = dfs(set(), graph2, key, initialCurrency, initial) 
            if amt != -1: 
                maxAmt = max(maxAmt, amt)

        return maxAmt 