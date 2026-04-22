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
        oldToNew = {}

        curr = head

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next] if curr.next else None
            copy.random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
        
        return oldToNew[head]
