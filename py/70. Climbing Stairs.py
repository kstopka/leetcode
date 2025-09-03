# https://leetcode.com/problems/climbing-stairs/description/
# Easy
# Math
# Dynamic Programming
# Memoization

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        stairsNumb = {0: 1, 1: 1}

        for x in range(2, n + 1):
            stairsNumb[x] = stairsNumb[x - 1] + stairsNumb[x - 2]

        return stairsNumb[n]

    def climbStairsV2(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairsV3(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        print(dp)
        dp[0] = dp[1] = 1
        print(dp)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairsV4(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            print(f"temp: {temp}")
            curr = prev + curr
            print(f"curr: {curr}")
            prev = temp
            print(f"prev: {prev}\n===============")

        return curr

    def climbStairsV5(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            print("start")
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
            print(memo)
        return memo[n]


cs = Solution()
# print(cs.climbStairsV5(2))
# print(cs.climbStairsV5(3))
# print(cs.climbStairsV5(4))
# print(cs.climbStairsV5(5))
# print(cs.climbStairsV5(6))
print(cs.climbStairsV5(7))


# 2 2-1 + 2-2
# 3
# 4
# 5
# 6
# 7
