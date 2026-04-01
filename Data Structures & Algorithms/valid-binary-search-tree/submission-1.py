# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # minVal < root.val < maxVal
        def isBST(root, minVal, maxVal):
            if not root:
                return True
            
            if root.val <= minVal or maxVal <= root.val:
                return False
            
            return (isBST(root.left, minVal, root.val) and
            isBST(root.right, root.val, maxVal))
        return isBST(root, float('-inf'), float('inf'))