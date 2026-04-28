# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(cur, path_max):
            if not cur:
                return 0
            
            good = 1 if cur.val >= path_max else 0
            path_max = max(path_max, cur.val)

            return good + dfs(cur.left, path_max) + dfs(cur.right, path_max)
        
        return dfs(root, root.val)