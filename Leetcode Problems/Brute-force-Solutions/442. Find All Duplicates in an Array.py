arr = [1,2,2,3,4,5,5,6]
def dup_count(arr):
    count = set()
    dups = []
    for i in arr:
        if i in count:
            dups.append(i)
        else:
            count.add(i)
    return dups
print(dup_count(arr))