arr = [1,1,2,2,3]
def removeDuplicates(arr):
    i=0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return arr[:i+1]
print(removeDuplicates(arr))