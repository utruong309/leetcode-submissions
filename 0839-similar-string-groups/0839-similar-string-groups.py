class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        
        adj = defaultdict(list)

        def isSimilar(word1, word2): 
            cnt = [] # idx that differ

            n = len(word1)

            for i in range(n): 
                if word1[i] != word2[i]: 
                    cnt.append(i)
            
            if len(cnt) != 2: 
                return False 
            
            first, sec = cnt[0], cnt[1]

            word1[first], word1[sec] = word1[sec], word1[first]

            return word1 == word2
        
        for i in range(len(strs) - 1): 
            for j in range(len(strs)): 
                w1 = list(strs[i])
                w2 = list(strs[j])
                if isSimilar(w1, w2): 
                    adj[strs[i]].append(strs[j])
                    adj[strs[j]].append(strs[i])
        
        cnt = 0 
        visited = set()  

        def dfs(word): 
            visited.add(word)

            for nei in adj[word]: 
                if nei not in visited: 
                    dfs(nei)

        
        for i in range(len(strs)): 
            if strs[i] not in visited: 
                dfs(strs[i])
                cnt += 1 
        
        return cnt