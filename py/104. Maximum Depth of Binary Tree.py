# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # result_left = 0
        # result_right = 0
        # if root.left:
        #     result_left = Solution().maxDepth(root.left)
        # if root.right:
        #     result_right = Solution().maxDepth(root.right)
        # print(result_left, result_right)
        # if result_left > result_right:
        #     result += result_left
        # if result_left < result_right:
        #     result += result_right
        # if result_left == result_right:
        #     result += result_left
        # return result


solution = Solution()

root = TreeNode(
    val=3,  # 1
    left=TreeNode(val=9),
    right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)),
)
print(solution.maxDepth(root))
