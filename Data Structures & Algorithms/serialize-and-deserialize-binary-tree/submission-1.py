# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []

        def helper(root):
            if not root:
                output.append('N')
                return
            output.append(str(root.val))
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return ','.join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque(data.split(','))
        
        def build():
            if not q:
                return
            curr = q.popleft()
            if curr == 'N':
                return None
            node = TreeNode(int(curr))
            node.left = build()
            node.right = build()

            return node
        return build()

            



