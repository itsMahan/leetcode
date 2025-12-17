from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        i = 0

        for num in nums:
            if num != i:
                return i
            else:
                i += 1

        return len(nums)


s = Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))