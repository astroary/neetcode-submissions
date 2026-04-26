# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None

        stack = []
        curr=head

        while curr:
            stack.append(curr)
            curr = curr.next

        curr= head
        for i in range(len(stack)//2):
            end = stack.pop()
            temp = curr.next
            curr.next = end
            end.next = temp
            curr = temp

        curr.next = None
