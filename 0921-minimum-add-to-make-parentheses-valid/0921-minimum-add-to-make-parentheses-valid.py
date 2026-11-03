class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        stack = [] 
        if open -> push to stack
        if close 
            if stack is empty -> add 1 to make it valid 
        if end of loop still have open brackets -> have to add that exact number of close 
        """
        stack = [] 
        cnt = 0 

        for ch in s: 
            if ch == '(': 
                stack.append(ch)
            else: 
                if not stack: 
                    cnt += 1 
                else: 
                    stack.pop() 
        
        cnt += len(stack)

        return cnt 