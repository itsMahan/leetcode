def singleNumber(nums):
    dic = dict()
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
        
    for k,v in dic.items():
        if v == 1:
            return k

print(SingleNumber([2,2,5,5,3,1,1,7,7]))
