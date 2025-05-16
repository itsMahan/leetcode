def twoSum(nums, target):
        i = 0
        size = len(nums)
        ls = list()
        while i < size:
            ls = nums[:]
            n = nums[i]
            for j in range(size):
                ls[j] += n
                #print("i={0}, j={1}, n={2}, ls[j]={3}".format(i, j, n, ls[j]))
                if ls[j] == target and i != j:
                    return i, j
            i += 1
            
        return None
