# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)
        while queue:
            currlen = len(queue)
            for i in range(currlen):
                this = queue.pop(0)
                if this.left:
                    queue.append(this.left)
                if this.right:
                    queue.append(this.right)
                if i == currlen - 1:
                        result.append(this.val)
        return result
                
            
