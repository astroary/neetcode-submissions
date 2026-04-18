# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            #1.move ptr
            nxt = curr.next
            #2 point curr to nothing
            curr.next = prev
            #3 point forward
            prev = curr
            curr = nxt
        
        return prev

        