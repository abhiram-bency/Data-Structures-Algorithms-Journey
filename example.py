s = "aabbcde"
def nonrepeat(s):
    pos = 1
    for i in range(1, len(s)):
        if s[i] != s[pos-1]:
            s[pos] = s[i]
            pos+=1
    return s[:pos]
print(nonrepeat(s))