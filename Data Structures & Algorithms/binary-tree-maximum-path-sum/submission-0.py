# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
            At every node we will choose:
            sendUp = max(root.val, root.val + leftPath, root.val.RightPath)
            TotalPath = (root.val + leftPath + rightPath) or sendUp)
            output = max(output, TotalPath)
        '''

        output = float('-inf')
        def dfs(root):
            nonlocal output

            if not root:
                return 0

            leftPath = dfs(root.left)
            rightPath = dfs(root.right)

            sendUp = max(root.val, root.val + leftPath, root.val + rightPath)

            totalPath = max(sendUp, root.val + leftPath + rightPath)
            output = max(output, totalPath)

            return sendUp
        
        dfs(root)
        return output
















