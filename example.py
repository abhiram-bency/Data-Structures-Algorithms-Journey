def solution(s):
    digits = []
    for i in s:
        if i.isdigit():
            digits.append(i)
    s = set(digits)
    if len(s)<2:
        result = -1
    else:
        l=list(s)
        l.remove(max(l))
        result=max(l)
    return result
    
s = "aabnsn1nnn2nbb36"
print(solution(s))