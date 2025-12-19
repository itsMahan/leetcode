from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        i = 1
        while i <= n:
            a, b = b, a + b
            i += 1

        return b


s = Solution()
print(s.climbStairs(2))