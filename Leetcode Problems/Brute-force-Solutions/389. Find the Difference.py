s = "ad"
t = "ade"

def find(s,t):
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in t:
        if i not in d or d[i]==0:
            return i
        d[i]-=1
print(find(s,t))