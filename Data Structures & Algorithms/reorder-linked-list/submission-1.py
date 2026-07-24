# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        secondhalf = []
        firsthalf = []
        fast = head
        slow = head
        finalpointer = head
        while fast != None and fast.next != None:
            firsthalf.append(slow)
            slow = slow.next
            fast = fast.next.next
        while slow != None:
            secondhalf.append(slow)
            slow = slow.next
        while firsthalf and secondhalf:
            finalpointer.next = firsthalf.pop(0)
            finalpointer = finalpointer.next
            finalpointer.next = secondhalf.pop()
            finalpointer = finalpointer.next
        if firsthalf:
            finalpointer.next = firsthalf.pop()
            finalpointer = finalpointer.next
        elif secondhalf:
            finalpointer.next = secondhalf.pop()
            finalpointer = finalpointer.next
        finalpointer.next = None
        
        