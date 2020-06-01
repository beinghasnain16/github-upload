# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert_tree(root):
            if root == None:
                return None
            root.left,root.right = root.right,root.left
            invert_tree(root.left)
            invert_tree(root.right)
            return root
        return invert_tree(root)
        
