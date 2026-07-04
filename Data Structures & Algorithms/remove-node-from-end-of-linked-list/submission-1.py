# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return 
        dummy = ListNode(0, head)
        removal, curr = dummy, head 

        for i in range(n):
            curr = curr.next
        
        while curr:
            removal = removal.next
            curr = curr.next
        removal.next = removal.next.next

        return dummy.next 