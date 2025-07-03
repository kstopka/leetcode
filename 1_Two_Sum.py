# https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/
# Easy
# Array
# Hash Table

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i  in range(n):
            search = target - nums[i]
            if search in numMap:
                return [numMap[search],i]
            numMap[nums[i]] = i
        return []


sums = Solution()
print(sums.twoSum([2,7,11,15],9))
print(sums.twoSum([3,2,4],6))
print(sums.twoSum([3,3],6))