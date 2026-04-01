# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = 0
        def helper(root):
            nonlocal output
            if not root:
                return 0
            
            leftLength = helper(root.left)
            rightLength = helper(root.right)
            output = max(output, leftLength+rightLength)
            return max(leftLength, rightLength) + 1
        helper(root)
        return output