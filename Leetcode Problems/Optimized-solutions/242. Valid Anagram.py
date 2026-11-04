t = "silent"
s = "listen"

def Valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in t:
        d[i] = d.get(i, 0) - 1
    for i in d:
        if d[i] != 0:
            return False
    return True
print(Valid_anagram(s,t))