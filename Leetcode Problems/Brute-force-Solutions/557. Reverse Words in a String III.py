s = "Reverse Words in a String III"
def reverseIII(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return " ".join(l)
print(reverseIII(s))