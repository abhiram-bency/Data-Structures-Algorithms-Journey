arr = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(arr)

for i in range(1, n):
    insert_index = i
    current_value = arr.pop(i)
    for j in range(n-i-1, -1, -1):
        if arr[j] > current_value:
            insert_index = j
    arr.insert(insert_index, current_value)
print(arr)