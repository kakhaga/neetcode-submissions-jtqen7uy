# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCount = 0

        def dfs(root, maxVal):
            nonlocal goodNodesCount
            if not root:
                return
            
            if root.val >= maxVal:
                maxVal = root.val
                goodNodesCount += 1
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, float('-inf'))
        return goodNodesCount          

            