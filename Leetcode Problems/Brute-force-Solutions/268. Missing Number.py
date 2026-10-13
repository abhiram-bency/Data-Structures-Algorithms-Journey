def missing_number(arr):
    n = len(arr)
    expected = n*(n+1)//2
    actual_sum = sum(arr)
    return expected - actual_sum
arr = (1,0,3)
print(missing_number(arr))