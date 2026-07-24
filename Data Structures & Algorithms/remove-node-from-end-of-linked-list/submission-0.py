# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1 = head
        length = 0
        pointer2 = head
        while pointer1 is not None:
            length += 1
            pointer1 = pointer1.next
        targetlocation = length - n
        if targetlocation == 0:
            head = head.next
            return head
        else:
            for i in range(targetlocation - 1):
                pointer2 = pointer2.next
            pointer2.next = pointer2.next.next
        return head

        