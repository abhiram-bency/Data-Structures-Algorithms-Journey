s = "Aabbbb"
#s = tree

def Sort_Characters_By_Frequency(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    result = ""
    for key in sorted(d, key = d.get, reverse=True):
        result += key*d[key]
    return result
print(Sort_Characters_By_Frequency(s))