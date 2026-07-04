# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(p, q):
            if not p and not q:
                return True
            elif (not p and q) or (not q and p) or (q.val != p.val):
                self.flag = False
                return False
            elif p.val == q.val:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
        dfs(p, q)
        return self.flag