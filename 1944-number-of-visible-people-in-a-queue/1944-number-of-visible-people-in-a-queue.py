class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        st = [] 
        right = len(heights) - 1 
        ans = [0] * len(heights)

        while right >= 0: 
            cnt = 0 

            while st and heights[right] > st[-1]: 
                cnt += 1 
                st.pop() 
            
            if st: 
                cnt += 1 # can see the leftmost taller person
            
            ans[right] = cnt 
            st.append(heights[right])
            right -= 1 
        
        return ans 