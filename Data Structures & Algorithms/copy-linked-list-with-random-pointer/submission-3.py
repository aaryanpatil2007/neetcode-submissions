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
        temp = head
        save = {}
        if not head:
            return None
        returnlist = Node(temp.val, None, None)
        returnlisthead = returnlist
        randpointer = returnlist
        temp2 = head
        while temp is not None:
            save[temp] = returnlisthead
            if temp.next:
                returnlisthead.next = Node(temp.next.val, None, None)
                returnlisthead = returnlisthead.next
            temp = temp.next
        while temp2 is not None:
            if temp2.random is None:
                randpointer.random = None
            else:
                randpointer.random = save[temp2.random]
            randpointer = randpointer.next
            temp2 = temp2.next
        return returnlist
