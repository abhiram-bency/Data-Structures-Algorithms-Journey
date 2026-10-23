arr = [1, 2, 2, 3, 3, 5]
def count_frequency(arr):
    new = []
    for i in range(0, len(arr)):
        if arr[i] in arr[:i]:
            continue
        k = 0
        for j in  range(len(arr)):
            if arr[j] == arr[i]:
                k+=1
        new.append([arr[i], k])
    return new
print(count_frequency(arr))