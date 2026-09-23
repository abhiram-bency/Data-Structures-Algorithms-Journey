def mergesort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sorted_left = mergesort(lefthalf)
    sorted_right= mergesort(righthalf)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result
arr = [64, 34, 25, 12, 22, 11, 90, 5]
print(mergesort(arr))