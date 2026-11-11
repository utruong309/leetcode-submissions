class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = {}

        def dfs(i, j): 
            if i == m: 
                return n - j 
            
            if j == n: 
                return m - i 
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else: 
                insert = dfs(i, j + 1)
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                dp[(i, j)] = 1 + min(insert, delete, replace)
            
            return dp[(i, j)]

        return dfs(0, 0)