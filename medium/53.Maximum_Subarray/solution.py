from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sum = 0

        for num in nums:
            if  curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sub = max(max_sub, curr_sum)

        return max_sub


s = Solution()
print(s.maxSubArray([-10, -8, -1, -5, -22]))