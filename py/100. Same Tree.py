from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (q is None) or (p is None):
            if q or p:
                return False
            return True
        result = True
        if p.val != q.val:
            result = False
        if result:
            result = Solution().isSameTree(p.left, q.left)
        if result:
            result = Solution().isSameTree(p.right, q.right)
        return result


root = TreeNode(
    val=1,
    left=TreeNode(val=2, left=TreeNode(val=2), right=TreeNode(val=5)),
    right=TreeNode(val=3),
)
root_2 = TreeNode(
    val=1,
    left=TreeNode(val=2, left=TreeNode(val=2), right=TreeNode(val=5)),
    right=TreeNode(val=3),
)
# root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))

solution = Solution()
print(solution.isSameTree(root, root_2))
