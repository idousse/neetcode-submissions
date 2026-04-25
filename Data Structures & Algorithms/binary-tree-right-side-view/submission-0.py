# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def rightDFS(cur, curDepth):
            if not cur:
                return

            if curDepth == len(res):
                res.append(cur.val)

            right = rightDFS(cur.right, curDepth + 1)
            left = rightDFS(cur.left, curDepth + 1)
        
        rightDFS(root, 0)

        return res