# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        ans = None

        def inorder(cur):
            nonlocal count, ans
            if not cur:
                return 0
            
            inorder(cur.left)
            count +=1
            if count == k:
                ans = cur.val
                return 
            inorder(cur.right)

        inorder(root)
        return ans
