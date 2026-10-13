arr = [1, 1, 2, 2, 3, 4, 4]
def remove_duplicates(arr):
    if not arr:
        return []
    pos = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[pos-1]:
            arr[pos] = arr[i]
            pos+=1
    
    #return arr[:pos]
    return pos
print(remove_duplicates(arr))