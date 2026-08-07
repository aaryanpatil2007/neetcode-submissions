# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currmax):
            if not root:
                return 0
            if root.val >= currmax:
                return 1 + dfs(root.left, max(root.val, currmax)) + dfs(root.right, max(root.val, currmax))
            elif root.val < currmax:
                return dfs(root.left, max(root.val, currmax)) + dfs(root.right, max(root.val, currmax)) 
        leftside = dfs(root.left, root.val)
        rightside = dfs(root.right, root.val)
        return 1 + leftside + rightside
        