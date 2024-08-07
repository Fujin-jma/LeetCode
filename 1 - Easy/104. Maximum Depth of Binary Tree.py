# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def runit(root):
            if root is None:
                return 0
            
            # Recur for the left and right subtrees
            ldepth = runit(root.left)
            rdepth = runit(root.right)
            
            # Return the maximum depth + 1 (for the current root)
            return max(ldepth, rdepth) + 1

        return runit(root)

       