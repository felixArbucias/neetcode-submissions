# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # index - 1
        myList = []
        # in order traversal of bst 
        def helper(root):
            if not root: # if it is null
                return
            helper(root.left)
            myList.append(root.val)
            helper(root.right) # full in order traversal 
        
        helper(root) # this will initialize the entire process 
        # now we have a complete set 

        return myList[k-1]

        

            