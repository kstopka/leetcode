# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Stack
# Tree
# Depth-First Search
# Binary Tree
from typing import Optional, List


# root = TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        current = root
        result = []

        if current.left:
            result.extend(Solution().inorderTraversal(current.left))

        result.append(current.val)

        if current.right:
            result.extend(Solution().inorderTraversal(current.right))

        return result


solution = Solution()
# root = TreeNode(val=1)
# root = TreeNode(val=1, left=TreeNode(val=2))
# root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
# root = TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))
root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(val=4, right=TreeNode(val=7, left=TreeNode(val=11))),
        right=TreeNode(
            val=5, left=TreeNode(val=8), right=TreeNode(val=9, right=TreeNode(val=12))
        ),
    ),
    right=TreeNode(val=3, left=TreeNode(val=6, left=TreeNode(val=10))),
)
print("wynik: ", solution.inorderTraversal(root))
