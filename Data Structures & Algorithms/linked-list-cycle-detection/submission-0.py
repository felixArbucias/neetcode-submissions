# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        keepTrack = set()
        curr = head
        while curr and curr.next:
            if curr.val in keepTrack:
                return True
            keepTrack.add(curr.val)
            curr = curr.next
        return False 
