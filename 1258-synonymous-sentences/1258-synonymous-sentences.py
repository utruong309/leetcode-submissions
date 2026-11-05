class Solution:
    def generateSentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        """
        Input: 
        synonyms[i] = [si, ti] -> si and ti are equivalent strings 
        text: str
        Output: All possible synonymous sentences 
        Approach: 
        - graph: {word: [list of synonyms]}
        - dfs to group synonyms
        - iterate thru text
            - try each option for each word
            - backtrack 
        """
        adj = defaultdict(list)

        for a, b in synonyms: 
            adj[a].append(b)
            adj[b].append(a)
        
        words = text.split() 
        n = len(words)
        lst = [0] * n 

        def dfs(word, res): 
            res.add(word)

            for nxt in adj[word]: 
                if nxt not in res: 
                    dfs(nxt, res)
            
        for i in range(n): 
            if words[i] not in adj: 
                lst[i] = [words[i]]
            else: 
                group = set() 
                dfs(words[i], group)
                lst[i] = list(group)
        
        # print(lst)
        ans = [] 

        def backtrack(idx, current): 
            if idx == n: 
                ans.append(" ".join(current[:]))
                return

            for w in lst[idx]: 
                current.append(w)
                backtrack(idx + 1, current)
                current.pop() 

        backtrack(0, [])

        ans.sort()

        return ans  