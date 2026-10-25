nums = [1,3,4,2,2]
def duplicate(nums):
    dups=[]
    for i in nums:
        if i in dups:
            return i
        else:
            dups.append(i)
print(duplicate(nums))