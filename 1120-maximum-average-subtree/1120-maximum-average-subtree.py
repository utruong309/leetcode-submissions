# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode | None) -> float:
        if not root: 
            return 0
        
        maxAvg = 0 

        def dfs(node): 
            nonlocal maxAvg 

            if not node: 
                return 0, 0 

            total = node.val 
            cnt = 1 

            left_total, left_cnt = dfs(node.left)
            right_total, right_cnt = dfs(node.right)

            total += left_total + right_total 
            cnt += left_cnt + right_cnt

            maxAvg = max(maxAvg, total / cnt)

            return total, cnt
        
        dfs(root)
        return maxAvg