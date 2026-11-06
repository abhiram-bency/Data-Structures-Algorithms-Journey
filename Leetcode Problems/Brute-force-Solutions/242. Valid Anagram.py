t = "silent"
s = "listen"

def anagram(s,t):
    if sorted(s)==sorted(t):
        return True
    else:
        return False
print(anagram(s,t))