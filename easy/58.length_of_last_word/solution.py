def lengthOfLastWord(s):

    s = " ".join(s.split())

    size = dict()
    
    words = s.split()

    return len(words[-1]) 




print(lengthOfLastWord("luffy is still joyboy"))
