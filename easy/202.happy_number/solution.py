def digits(n):
    digits = list()

    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    
    digits.reverse()
    return digits

# print(digits(1356))
# print(int(''.join(str(x) for x in digits(1467))))

used_nums = list()

def isHappy(n):

    if n == 1:
        return True
    
    global used_nums
    used_nums.append(n)

    numbers = digits(n)

    squared_numbers = list(map(lambda x: x**2 , numbers))

    res = 0

    for num in squared_numbers:
        res += num

    if res in used_nums:
        return False

    elif res == 1:
        return True

    else:
        return isHappy(res)

print(isHappy(19))
