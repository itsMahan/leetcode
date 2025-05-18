def firstUniqChar(s):
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1

    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i
    return -1

#firstUniqChar("dddccdbba")
print(firstUniqChar("dddccdbba"))

