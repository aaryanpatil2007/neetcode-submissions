# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #check left
        #check self
        #check right
        self.finallist = []
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            self.finallist.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return all(self.finallist[i + 1] > self.finallist[i] for i in range(len(self.finallist) - 1))
        
