# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: return False
        elif subRoot is None: return True
        elif self.same(root,subRoot): return True
        else: return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, r, sr):
        if r is None and sr is None: return True
        elif r and sr and (r.val == sr.val):
            return self.same(r.left,sr.left) and self.same(r.right,sr.right)
        else: return False