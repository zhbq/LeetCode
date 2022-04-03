from operator import mod


nums1 = input().split()
nums2 = input().split()

nums1 = [int(i) for i in nums1]
nums2 = [int(i) for i in nums2]

for i in range(len(nums2)):
    nums1.append(nums2[i])

nums1.sort()
l = len(nums1)

if mod(l,2) == 0:
    result = (nums1[int(l/2)] + nums1[int(l/2-1)])/2
else:
    result = nums1[int((l-1)/2)]

print(type(result))
