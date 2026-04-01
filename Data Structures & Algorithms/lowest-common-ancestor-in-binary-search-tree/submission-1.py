# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def helper(root, p, q):
            if not root or not p or not q:
                return None
            
            if root.val < p.val and root.val < q.val:
                return helper(root.right, p,q)
            
            elif p.val < root.val and q.val < root.val:
                return helper(root.left, p , q)
            
            else:
                return root
        
        return helper(root,p,q)
            

