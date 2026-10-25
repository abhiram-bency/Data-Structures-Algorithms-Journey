arr = [1,2,3,4,4,5]
def duplicate(arr):
    dup = []
    for i in arr:
        if i in dup:
            return i
        else:
            dup.append(i)
print(duplicate(arr))