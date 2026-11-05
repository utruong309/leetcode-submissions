class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        Input: 
        accounts[i][0]: name 
        accounts[i][1:]: emails
        - merge if have common email
        - 2 ppl can have the same name 
        Output: 
        [[name, email1, email2, email3]]
        Approach: 
        - need to keep track of email -> name for output 
        - graph: {email: [list of emails in the same account]}, all point to just 1 root email
        - dfs to merge emails 
        """
        adj = defaultdict(list)
        names = {}
        ans = [] 

        for entry in accounts: 
            name = entry[0]
            emails = entry[1:]
            root = emails[0]
            adj[root].append(root)
            names[root] = name

            for email in emails[1:]: 
                names[email] = name 
                adj[root].append(email)
                adj[email].append(root)
        
        visited = set() 
        
        def dfs(email, lst): 
            visited.add(email)
            lst.append(email)

            for nxt in adj[email]: 
                if nxt not in visited: 
                    dfs(nxt, lst)
        
        for key in names: 
            if key in visited: 
                continue 
            temp = [] 
            dfs(key, temp)
            temp.sort()
            temp.insert(0, names[key])
            ans.append(temp)

        return ans