# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isequal(root, subroot):
            if not root and not subroot:
                return True
            if not root:
                if subroot:
                    return False
            if not subroot:
                if root:
                    return False
            if root.val != subroot.val:
                return False
            return isequal(root.left, subroot.left) and isequal(root.right, subroot.right)
        
        answer = isequal(root, subRoot)
        if answer:
            return answer
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

