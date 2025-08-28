# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left = Solution().invertTree(root.right)
        right = Solution().invertTree(root.left)
        return TreeNode(val=root.val, left=left, right=right)


root = TreeNode(
    val=2,
    left=TreeNode(val=1),
    right=TreeNode(val=3),
)

solution = Solution()
print(solution.invertTree(root))
