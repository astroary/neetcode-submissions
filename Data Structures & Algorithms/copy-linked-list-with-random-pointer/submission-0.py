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
        if head is None:
            return None
        
        oldToNew = {None: None}
        curr = head
        while curr:
            # make a copy of the nodes in pass 1
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next
        curr=head

        while curr:
            # get clone and assign its next and random
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]