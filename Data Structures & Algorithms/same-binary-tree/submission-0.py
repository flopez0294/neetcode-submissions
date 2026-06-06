# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        stackp = [p]
        stackq = [q]
        while stackq and stackp:
            nodep = stackp.pop()
            nodeq = stackq.pop()
            if nodep is None and nodeq is None:
                continue
            elif nodep is None or nodeq  is None:
                return False
            if nodep.val != nodeq.val:
                return False
            stackp.append(nodep.left)
            stackp.append(nodep.right)
            stackq.append(nodeq.left)
            stackq.append(nodeq.right)
        
        return True