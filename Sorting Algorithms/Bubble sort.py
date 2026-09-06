arr = [20, 14, 2, 45]

n = len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
print(arr)