def second_max_digit(s):
    digits = []
    for i in s:
        if i.isdigit():
            digits.append(int(i))
    s = set(digits)
    if len(s)<2:
        result = -1
    else:
        l = list(s)
        l.remove(max(l))
        result = max(l)
    return result
s="abcs1b2b0cc6d"
print(second_max_digit(s))