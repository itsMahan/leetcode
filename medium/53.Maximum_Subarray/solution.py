from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i

        i, j = max_index - 1, max_index + 1
        sum, max_sum = nums[max_index], nums[max_index]

        while i >= 0:
            if sum + nums[i] > max_sum:
                sum += nums[i]
                max_sum = sum
            else:
                sum += nums[i]
            i -= 1

        sum = max_sum

        while j < len(nums):
            if sum + nums[j] > max_sum:
                sum += nums[j]
                max_sum = sum
            else:
                sum += nums[j]
            j += 1

        return max_sum


s = Solution()
print(s.maxSubArray([3,-2,-3,-3,1,3,0]))