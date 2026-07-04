# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()

        if root:
            q.append(root)
        

        res = []
        
        while q: # while there are nodes in the q, we keep going 

            lvl = [] # resetting after every new level

            for i in range(len(q)): # empty the q, be reset when we add more stuff to the q 
                curr = q.popleft()
                lvl.append(curr.val)

                if curr.left: # checking not null
                    q.append(curr.left) # adding left to the q 
                
                if curr.right: # checking not null 
                    q.append(curr.right) # adding it to the q 
            
            res.append(lvl)

        return res 