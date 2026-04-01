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

        def dfs(root):
            nonlocal output
            if not root:
                output.append('N')
                return
            
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque(data.split(','))

        def build():
            nonlocal q
            if not q:
                return None
            val = q.popleft()

            if val == 'N':
                return None
            
            node = TreeNode(val)
            node.left = build()
            node.right = build()

            return node
        return build()









