nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
sum = 14
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == sum:
            result.append(i)
            result.append(j)
print(result)