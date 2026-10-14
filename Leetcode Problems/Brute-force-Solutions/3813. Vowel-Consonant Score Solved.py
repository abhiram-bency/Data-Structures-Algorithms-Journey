def score(s):
    v=0
    c=0
    for ch in s:
        if ch.isalpha():
            if ch in "aeiou":
                v+=1
            else:
                c+=1
    if c==0:
        return 0
    return v//c

s="aaeplaiotu"
print(score(s))