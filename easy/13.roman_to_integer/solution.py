def romanToInt(s):
        
    romans = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000 , 'z':0}

    res = 0

    s = s + 'z'
    i = 0
    while(i < len(s) - 1):
        if romans[s[i]] < romans[s[i+1]]:
            res = res + (romans[s[i+1]] - romans[s[i]])
            i += 2
        else:
            res += romans[s[i]]
            i += 1

    return res

print(romanToInt("MCMXCIV"))

