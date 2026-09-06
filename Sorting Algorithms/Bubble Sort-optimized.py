arr = [10, 45, 1, 23, 12]

n = len(arr)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if arr[j] > arr[i]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
print(arr)