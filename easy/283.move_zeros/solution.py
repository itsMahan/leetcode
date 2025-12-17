from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:

        l, r = 0, 1

        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1

        return nums


s = Solution()
print(s.moveZeroes([1, 3, 4, 0, 2, 0]))