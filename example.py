arr = [ 7,12,9,11,3 ]
def second_max(arr):
    max_el = arr[0]
    second = -1
    for i in range(len(arr)):
        if arr[i] > max_el:
            second = max_el
            max_el = arr[i]
        elif max_el > arr[i] > second:
            second = arr[i]
    return second
print(second_max(arr))