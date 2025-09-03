from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:

#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if (q is None) or (p is None):
#             if q or p:
#                 return False
#             return True
#         result = True
#         if p.val != q.val:
#             result = False
#         if result:
#             result = Solution().isSameTree(p.left, q.left)
#         if result:
#             result = Solution().isSameTree(p.right, q.right)
#         return result

#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return None
#         left = Solution().invertTree(root.right)
#         right = Solution().invertTree(root.left)
#         return TreeNode(val=root.val, left=left, right=right)

#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if (root.left is None) or (root.right is None):
#             if root.left or root.right:
#                 return False
#             return True

#         right = Solution().invertTree(root.right)
#         left = root.left

#         return Solution().isSameTree(left, right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(n1, n2):  # n1:left, n2:right
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return (
                n1.val == n2.val
                and is_mirror(n1.left, n2.right)
                and is_mirror(n1.right, n2.left)
            )

        return is_mirror(root.left, root.right)


# rozwiązanie
# w pierwszym kroku zamienić right z left
# w drugim kroku porównać czy są takie same

root = TreeNode(
    val=1,
    left=TreeNode(
        val=2, left=TreeNode(val=4, left=TreeNode(val=5)), right=TreeNode(val=3)
    ),
    right=TreeNode(
        val=2, right=TreeNode(val=4, right=TreeNode(val=5)), left=TreeNode(val=3)
    ),
)
# root = TreeNode(
#     val=1,
#     left=TreeNode(val=2, left=TreeNode(val=3)),
#     right=TreeNode(val=2, right=TreeNode(val=3)),
# )


solution = Solution()
# print(solution.invertTree(root))
print(solution.isSymmetric(root))
