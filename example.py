arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
def countingsort(arr):
    max_value = max(arr)
    count = [0] * (max_value+1)

    for num in arr:
        count[num] +=1

    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)
    return arr
print(countingsort(arr))