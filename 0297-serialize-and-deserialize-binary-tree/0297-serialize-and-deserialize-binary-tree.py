# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return 'X'
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        # print(str(root.val), left, right)
        return f"{root.val},{left},{right}"

    def deserialize(self, data):
        nodes = data.split(',')

        def traverse():
            node_val = nodes.pop(0)
            if node_val == 'X':
                return None
            
            node = TreeNode(int(node_val))
            node.left = traverse()
            node.right = traverse()
            return node

        return traverse()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))