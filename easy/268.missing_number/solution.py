from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        expected_total = 0
        total = 0

        for i in range(n+1):
            expected_total += i

        for num in nums:
            total += num

        return expected_total - total



s = Solution()
print(s.missingNumber([1, 0, 3]))