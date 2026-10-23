arr = [0,1,1,2,2,3,3,3,4]
def count_freq(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    new = []
    for i in freq:
        new.append([i, freq[i]])
    return new
print(count_freq(arr))