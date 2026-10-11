# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # since we know that the left child is 2i + 1 and the right 
        # child is 2i + 2, we can invert the binary tree by swapping the
        # left and right child if the parent has children

        # inverting a binary tree means look at every single node and every
        # time you do so look at its two children and swap the positions of
        # the children. 

        # since we're not given an array representation we recursively go into
        # the children and swap (depth first search)
        if not root:
            return None

        temporary = root.left
        root.left = root.right
        root.right = temporary

        # preorder traversal (root -> left -> right)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

