class Solution:
    def decodeString(self, s: str) -> str:
        """
        3[a]2[bc]
        aaabcbc

        helper(idx, res) # only append to res if char 
        open: [number][
            length = number 
            s = helper(idx + 1, [])
            output.append(length * s)
        close: ]
            return res -> return the string 
        char: 
            res.append(s[idx])
            return helper(idx + 1, res) so we could return the resulted string upward

            actually if a number we need to get the final length first 
        """
        def helper(idx, res): 
            length = 0 

            if idx == len(s): 
                return idx, res 
                
            if s[idx].isdigit(): 
                while s[idx].isdigit(): 
                    length = length * 10 + int(s[idx])
                    idx += 1 
                
                # idx is now [
                # want to know next avail idx and also the inner string 
                nxt, inner = helper(idx + 1, [])
                res.extend(length * inner)
                return helper(nxt + 1, res)
            elif s[idx] == ']':
                return idx, res 
            else: 
                res.append(s[idx])
                return helper(idx + 1, res)
        
        return "".join(helper(0, [])[1])