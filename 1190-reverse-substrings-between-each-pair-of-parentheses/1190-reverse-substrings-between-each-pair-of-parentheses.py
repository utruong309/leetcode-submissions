class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        def helper(idx, res):
            if idx == len(s): 
                return idx, res 
            if s[idx] == '(':
                # get the reversed string from this level 
                nxt, inner = helper(idx + 1, [])
                res.extend(reversed(inner))
                return helper(nxt + 1, res)
            elif s[idx] == ')': 
                return idx, res 
            else: 
                res.append(s[idx]) 
                return helper(idx + 1, res)

        
        return "".join(helper(0, [])[1])