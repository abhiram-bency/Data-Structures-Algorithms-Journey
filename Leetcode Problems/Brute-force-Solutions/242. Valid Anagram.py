def anagram(t,s):

    if sorted(t) == sorted(s):
        return True
    else:
        return False
t = "silent"
s = "listen"
print(anagram(t,s))