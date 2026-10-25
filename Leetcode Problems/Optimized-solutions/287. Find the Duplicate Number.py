arr = [1,2,3,4,4,5]
def duplicates(arr):
    dups = set()
    for i in arr:
        if i in dups:
            return i
        else:
            dups.add(i)

print(duplicates(arr))