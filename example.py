s = "hello"
def solve(s):
    i=0
    sum = 0
    for j in range(1, len(s)):
        sum += abs(ord(s[i])-ord(s[j]))
        i+=1
    return sum
print(solve(s))