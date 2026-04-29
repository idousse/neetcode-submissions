# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []
        ans = None

        def inorder(cur):
            nonlocal arr, ans
            if not cur:
                return 0
            
            inorder(cur.left)
            arr.append(cur.val)
            if len(arr) == k:
                ans = cur.val
            inorder(cur.right)

        inorder(root)
        return ans
