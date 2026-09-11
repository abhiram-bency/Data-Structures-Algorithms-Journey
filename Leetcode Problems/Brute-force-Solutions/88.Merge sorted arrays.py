nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

for i in range(0, len(nums2)):
    nums1.append(nums1[i])

l = len(nums2)
for i in range(l-1):
    swapped  = False
    for j in range(l-i-1):
        if nums1[j]>nums1[j+1]:
            nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
            swapped = True
    if not swapped:
        break
while 0 in nums1:
    nums1.remove(0)
print(nums1)