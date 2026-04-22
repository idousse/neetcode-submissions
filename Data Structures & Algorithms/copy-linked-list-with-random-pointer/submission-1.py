"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head

        while cur:
            newnode = Node(cur.val,cur.next)
            cur.next = newnode
            cur = newnode.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        oldhead = head
        newhead = head.next
        oldcur = oldhead
        newcur = newhead

        while oldcur:
            oldcur.next = oldcur.next.next
            newcur.next = newcur.next.next if newcur.next else None
            oldcur = oldcur.next
            newcur = newcur.next
        
        return newhead

        