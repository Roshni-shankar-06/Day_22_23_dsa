class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        vals = iter(data.split(","))
        
      
