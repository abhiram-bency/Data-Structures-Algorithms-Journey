arr = [10, 7, 0, -1, 3, 8, 0, 1]
def second_max(arr):
    largest = float("-inf")
    second = float("-inf")
    for nums in range(len(arr)):
        if arr[nums] > largest:
            second = largest
            largest = arr[nums]
        elif largest > arr[nums] > second:
            second = arr[nums]
    if second == float("-inf"):
        return -1
    return second
print(second_max(arr))