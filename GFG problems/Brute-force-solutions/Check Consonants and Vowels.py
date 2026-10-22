def vowel_consonents(s):
    v=0
    c=0
    for ch in s:
        if ch in "aeiou":
            v+=1
        else:
            c+=1
    if v>c:
        print("Yes")
    elif v<c:
        print("No")
    else:
        print("Same")
s = "thequickbrownfoxjumpsoverthelazydog"
print(vowel_consonents(s))