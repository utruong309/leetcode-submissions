class Solution:
    def areSentencesSimilarTwo(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        """
        - create adj list from similarPairs 
        - dfs on each word of sentence1 and sentence2 to see if one word can reach another
        """
        if len(sentence1) != len(sentence2): 
            return False 
        
        adj = defaultdict(list)

        for w1, w2 in similarPairs: 
            adj[w1].append(w2)
            adj[w2].append(w1)
        
        def dfs(start, target, visited): 
            if start == target: 
                return True 
            
            visited.add(start)

            for nxt in adj[start]: 
                if nxt not in visited: 
                    if dfs(nxt, target, visited): 
                        return True 
            
            return False 
        
        n = len(sentence1)

        for i in range(n): 
            if sentence1[i] == sentence2[i]: 
                continue 
            if not dfs(sentence1[i], sentence2[i], set()): 
                return False 
        
        return True 