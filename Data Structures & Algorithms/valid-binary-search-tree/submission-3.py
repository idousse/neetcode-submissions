# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def inorder(cur):
            nonlocal prev
            if not cur:
                return True

            if not inorder(cur.left):
                return False
            
            if cur.val <= prev:
                return False
            
            prev = cur.val
            return inorder(cur.right)

        return inorder(root)
        