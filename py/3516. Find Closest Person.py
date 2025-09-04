# https://leetcode.com/problems/find-closest-person/description


class Solution:
    def findCloset(self, x: int, y: int, z: int) -> int:
        x_steps = abs(x - z)
        y_steps = abs(y - z)
        if x_steps > y_steps:
            return 1
        elif x_steps < y_steps:
            return 2
        else:
            return 0


solution = Solution()
solution.findCloset(2, 7, 4)
