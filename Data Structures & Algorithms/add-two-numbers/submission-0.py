# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # putting the values and checking if null
            v2 = l2.val if l2 else 0 # putting value from l2 and checking if null 

            val = v1 + v2 + carry
            carry = val // 10 
            # 6+9 = 15
            # the carry: 15 // 10 = 1 
            # the actual value being made into a new node is 15 % 10 = 5 
            val = val % 10
            cur.next = ListNode(val) # making a new node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
    
        return dummy.next
            

 