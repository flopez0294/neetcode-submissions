# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        nodeIdx = size - n
        curr = head
        print(size)
        if size == 1:
            return None
        if size == n:
            return head.next
        size = 0
        while curr:
            print(curr.val)
            if nodeIdx - 1 == size:
                curr.next = curr.next.next
            curr = curr.next
            size += 1
        return head