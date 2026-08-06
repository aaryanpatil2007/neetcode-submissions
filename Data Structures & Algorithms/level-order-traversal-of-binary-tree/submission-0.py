# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resultlist = []
        if not root:
            return []
        queue = []
        queue.append(root)
        while queue:
            currlen = len(queue)
            thislevel = []
            for i in range(currlen):
                thisval = queue.pop(0)
                thislevel.append(thisval.val)
                if thisval.left:
                    queue.append(thisval.left)
                if thisval.right:
                    queue.append(thisval.right)
            resultlist.append(thislevel)
        return resultlist
                





