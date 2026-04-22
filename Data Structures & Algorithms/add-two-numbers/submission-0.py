# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0,None)
        rest = digit = 0
        node = head

        while l1 or l2 or rest:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            num = v1 + v2

            total = num + rest
            digit = total % 10
            rest = total // 10

            node.val = digit

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
  
            if l1 or l2 or rest:
                newnode = ListNode(0,None)
                node.next = newnode
                node = newnode

        return head
        

