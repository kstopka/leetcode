# https://leetcode.com/problems/sqrtx/description/# Easy
# Math
# Binary Search


class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt_number = 0
        # while x > sqrt_number * sqrt_number:
        #     sqrt_number += 1
        #     if sqrt_number * sqrt_number > x:
        #         return sqrt_number - 1

        # return sqrt_number
        if x == 0:
            return 0

        first, last = 1, x

        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1

        return last


sqrt = Solution()
# print(sqrt.mySqrt(0))
# print(sqrt.mySqrt(1))
# print(sqrt.mySqrt(4))
# print(sqrt.mySqrt(8))
# print(sqrt.mySqrt(10))
# print(sqrt.mySqrt(25))
# print(sqrt.mySqrt(26))
# print(sqrt.mySqrt(36))
print(sqrt.mySqrt(38))
