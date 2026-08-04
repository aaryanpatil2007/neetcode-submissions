# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add the two numbers + carryover
        # if greater than 10 then second digit is carryover
        # add carryover + two numbers for next round
        # if one list finishes first 
        returnlist = ListNode(None, None)
        dummynode = returnlist
        carryover = 0
        while l1 and l2:
            currval = l1.val + l2.val + carryover
            if currval >= 10:
                carryover = 1
                returnlist.val = currval % 10
                returnlist.next = ListNode(None, None)
                returnlist = returnlist.next
                l1 = l1.next
                l2 = l2.next
            else:
                returnlist.val = currval
                carryover = 0
                if l1.next or l2.next:
                    returnlist.next = ListNode(None, None)
                    returnlist = returnlist.next
                l1 = l1.next
                l2 = l2.next
        if l1:
            while l1:
                currval = l1.val + carryover
                if currval >= 10:
                    carryover = 1
                    returnlist.val = currval % 10
                    returnlist.next = ListNode(None, None)
                    returnlist = returnlist.next
                    l1 = l1.next
                else:
                    returnlist.val = currval
                    carryover = 0
                    if l1.next:
                        returnlist.next = ListNode(None, None)
                        returnlist = returnlist.next
                    l1 = l1.next
        elif l2:
            while l2:
                currval = l2.val + carryover
                if currval >= 10:
                    carryover = 1
                    returnlist.val = currval % 10
                    returnlist.next = ListNode(None, None)
                    returnlist = returnlist.next
                    l2 = l2.next
                else:
                    returnlist.val = currval
                    carryover = 0
                    if l2.next:
                        returnlist.next = ListNode(None, None)
                        returnlist = returnlist.next
                    l2 = l2.next
        if carryover:
            returnlist.val = carryover
        return dummynode
