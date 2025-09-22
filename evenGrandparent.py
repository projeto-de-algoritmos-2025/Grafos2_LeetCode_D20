# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        def dfs(no, pai, avo):
            if not no:
                return 0
            
            total = 0
            if avo and avo.val % 2 == 0:
                total += no.val # avo eh par

            total += dfs(no.left, no, pai)
            total += dfs(no.right, no, pai)

            return total
        
        return dfs(root, None, None) # caso trivial