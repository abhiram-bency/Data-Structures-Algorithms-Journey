s = "abcdefg"
k = 2

def reverse(s,k):
    l = list(s)
    i=0
    while i<len(l):
        l[i:i+k] = l[i:i+k][::-1]
        i+=2*k
    return "".join(l)
print(reverse(s,k))