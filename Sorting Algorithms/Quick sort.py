arr = [64, 34, 25, 12, 22, 11, 90, 5]

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i+=1
            array[i], arr[j] = arr[j], arr[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)

quick_sort(arr)
print(arr)