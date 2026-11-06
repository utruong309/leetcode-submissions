class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False] * (n + 1)
        cnt = 0 

        def backtrack(pos): 
            nonlocal cnt 
            if pos == n + 1: 
                cnt += 1 
                return 
            
            for num in range(1, n + 1): # pick a number to fill in current pos 
                if not used[num] and (num % pos == 0 or pos % num == 0): 
                    print(num)
                    used[num] = True 
                    backtrack(pos + 1)
                    used[num] = False # try different number for current pos 
        
        backtrack(1)

        return cnt 