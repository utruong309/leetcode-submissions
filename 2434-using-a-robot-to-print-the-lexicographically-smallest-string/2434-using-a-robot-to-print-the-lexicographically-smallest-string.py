class Solution:
    def robotWithString(self, s: str) -> str:
        """
        only print from t to paper if top of t is smaller than every remaining character in s

        - iterate thru every character in s 
        - push that letter to t 
        - update the min letter in s when we have already pulled the prev to t 
        - min letter starts at 'a' 
        - so while min_letter not in freq or freq[min_letter] == 0: 
            min_letter = chr(ord(min_letter) + 1)
        - if top of t <= min_letter -> print to paper 
        """
        t = []
        freq = {} # to keep track of how many letters we have left in s

        for c in s: 
            freq[c] = freq.get(c, 0) + 1 
        
        min_letter = 'a'
        res = [] 

        for c in s: 
            t.append(c)
            freq[c] -= 1 

            while min_letter <= 'z' and freq.get(min_letter, 0) == 0: 
                min_letter = chr(ord(min_letter) + 1)

            while t and t[-1] <= min_letter: 
                res.append(t.pop())
        
        return "".join(res)