# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        center = len(nums) // 2
        left = nums[:center]
        right = nums[center + 1 :]
        return TreeNode(
            val=nums[center],
            left=self.sortedArrayToBST(left),
            right=self.sortedArrayToBST(right),
        )


sol = Solution()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sol.sortedArrayToBST(nums)
