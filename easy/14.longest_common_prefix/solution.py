def longestCommonPrefix(strs):

    def find_smallest():
        min_item = strs[0]

        for i in range(1, len(strs)):
            if len(strs[i]) < len(min_item):
                min_item = strs[i]
            
        return min_item

    min_item = find_smallest()

    res = ""

    for i in range(len(min_item)):
        flag = 1
        for st in strs:
           if st[i] != min_item[i]:
               flag = 0
               break
        if flag == 1:
           res += min_item[i]
        else:
            break

    return res

print(longestCommonPrefix(["cir", "car"]))

