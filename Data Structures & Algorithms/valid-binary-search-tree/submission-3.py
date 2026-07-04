# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.true = True 
        def valid(root, left, right): 
            # root cannot be less than left bound
            # root cannot be greater than right bound 
            if not root:
                return True 
            
            if (root.val <= left or root.val >= right):
                self.true = False 
                return False 
            
            valid(root.left, left, root.val)
            valid(root.right, root.val, right)
        
        valid(root, float('-inf'), float('inf'))
        return self.true

