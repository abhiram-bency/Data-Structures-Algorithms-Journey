s = "Let's take LeetCode contest"

def reverse(s):
    l=s.split()
    i = 0
    for i in range(0, len(l)):
        l[i] = l[i][::-1]
    return " ".join(l)
print(s)
print(reverse(s))