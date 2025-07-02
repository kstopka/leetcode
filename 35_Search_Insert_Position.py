# https://leetcode.com/problems/search-insert-position/description/
# Easy
# Array
# Binary Search
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for idx, x in enumerate(nums):
        #     if x == target:
        #         return idx
        #     elif x < target and idx + 1 == len(nums):
        #         return len(nums)
        #     elif x < target and nums[idx + 1] > target:
        #         return idx + 1

        # return 0
        
        for idx, x in enumerate(nums):
            if(x >= target): return idx
        return len(nums)

sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 7))