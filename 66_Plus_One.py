# https://leetcode.com/problems/plus-one/description/
# Easy
# Array
# Math

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


plus = Solution()
print(plus.plusOne([3,2,4,9]))
print(plus.plusOne([9,9,9,9,9,9]))
print(plus.plusOne([1,2,3]))
print(plus.plusOne([4,3,2,1]))
print(plus.plusOne([9]))
print(plus.plusOne([0]))
print(plus.plusOne([]))