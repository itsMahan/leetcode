def isAnagram(s, t):
    if len(s) != len(t):
        return False
    size = len(s)
    s_dict = dict()
    t_dict = dict()
    for i in range(size):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 0
        
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 0
    
    if s_dict == t_dict:
        return True
    else:
        return False
    
#print(isAnagram("nagaraddm", "anagram"))
