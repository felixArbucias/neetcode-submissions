# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.true = True 

        def traverse(rootP, rootQ):
            if not rootP and not rootQ:
                return 
            elif not rootP and rootQ or not rootQ and rootP:
                self.true = False 
                return 
            elif rootP.val != rootQ.val:
                self.true = False
            
            traverse(rootP.left, rootQ.left)
            traverse(rootP.right, rootQ.right)
        
        traverse(p, q)
        return self.true 
