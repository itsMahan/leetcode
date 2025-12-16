from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pivot = int(len(nums)/2)
        num_occ = dict()

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            key = str(num)

            try:
                if num_occ[key]:
                    num_occ[key] += 1
                if num_occ[key] > pivot:
                    return num
            except KeyError:
                num_occ[key] = 1



s = Solution()
print(s.majorityElement([1]))