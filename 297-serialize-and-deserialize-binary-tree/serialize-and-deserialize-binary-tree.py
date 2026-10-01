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
            
   
        
      
