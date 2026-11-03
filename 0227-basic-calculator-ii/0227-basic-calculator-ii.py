class Solution:
    def calculate(self, s: str) -> int:
        """
        Input: string s 
        Ouput: result of expression 

        3+2*2 
        * / should be computed immediately, + - later 
        3+2*2 -> 3 + (2 * 2)
        3-2*2 -> 3 + (-2 * 2)

        sum of
        -a
        a
        (a*b)
        (a/b)

        num = 0 # the num we're building
        op = +

        iterate thru s: 
            if digit: 
                num = 10 * num + digit
            else: 
                done with the num 
                push to stack with the op to its left 
                if * or / then need to modify the most recent term -> pop top of stack */ num -> push to stack again 
        
        return sum of stack 
        """
        stack = [] 
        num = 0 
        op = '+'
        s = s.replace(" ", "")

        for i, ch in enumerate(s): 
            if ch.isdigit(): 
                num = 10 * num + int(ch)
                # print(num)

            if not ch.isdigit() or i == len(s) - 1:  
                if op == '+': 
                    stack.append(num)
                elif op == '-': 
                    stack.append(-num)
                elif op == '*': # 3 * 2 - 2
                    first = stack.pop() 
                    stack.append(first * num)
                else: 
                    first = stack.pop() 
                    stack.append(int(first / num))
                
                num = 0 
                op = ch
        
        return sum(stack)