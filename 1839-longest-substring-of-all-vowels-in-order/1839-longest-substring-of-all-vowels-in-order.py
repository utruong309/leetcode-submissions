class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maxLength = 0 
        length = 1 
        kinds = 1
        n = len(word)

        for i in range(1, n): 
            if word[i] >= word[i - 1]: 
                length += 1 
                if word[i] > word[i - 1]: 
                    kinds += 1 
                
                if kinds == 5: 
                    maxLength = max(maxLength, length)
            else: 
                length = 1 
                kinds = 1 
        
        return maxLength