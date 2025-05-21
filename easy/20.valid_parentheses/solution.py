def isValid(s):
    stack = list()
    
    if s[0] in [ ')', '}', ']' ]:
        return False

    for i in range(len(s)):
        if s[i] in [ '(', '[', '{' ]:
            stack.append(s[i])
            continue

        if (s[i] == ')') and (len(stack) != 0):
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif (s[i] == '}') and (len(stack) != 0):
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif (s[i] == ']') and (len(stack) != 0):
            if stack[-1] == '[':
                stack.pop()
            else:
                return False

        else:
            return False

    if len(stack) == 0:
        return True

    return False

print(isValid("(])"))

