jewels= "aA"
stones = "aaAbbbb"

def jewel_count(jewels, stones):
    count = 0
    j = {}
    s = {}
    for i in jewels:
        j[i] = j.get(i, 0) + 1
    for i in stones:
        s[i] = s.get(i, 0) + 1

    for i in s:
        if i in j:
            count += s[i]
    return count
print(jewel_count(jewels, stones))