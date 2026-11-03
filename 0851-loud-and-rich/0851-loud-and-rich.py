class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        """
        Input: 
        - n people
        - richer[i] = [ai, bi] -> a richer than b
        - quiet[i] = quietness of ith person
        Output: 
        answer array, answer[x] = y if y is the least quiet but richer than x 
        Approach: 
        {a: [list of people who richer than a]} -> dfs on initial graph 
        find the least quiet person among those 
        """
        n = len(quiet)
        adj = defaultdict(list)
        ans = []

        for a, b in richer: 
            adj[b].append(a)
        
        def dfs(person, lst): 
            lst.add(person)

            for nei in adj[person]: 
                if nei not in lst: 
                    dfs(nei, lst)
        
        for i in range(n): 
            temp = {i}

            for nei in adj[i]: 
                dfs(nei, temp)
            
            adj[i] = list(temp)
        
        # print(adj)

        def findMin(lst): 
            res = lst[0]

            for nei in lst: 
                if  quiet[nei] < quiet[res]: 
                    res = nei
            
            return res 
        
        for i in range(n): 
            min_person = findMin(adj[i])
            ans.append(min_person)
        
        return ans