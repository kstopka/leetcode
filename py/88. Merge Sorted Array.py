# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = [10]
        nums1.sort()


merge = Solution()

merge.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
