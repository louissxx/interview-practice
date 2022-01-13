# def findmedian(nums1, nums2):
#     mid1 = nums1[len(nums1)//2]
#     mid2 = nums2[len(nums2)//2]
#     sum = 0
#     if mid1 > mid2:
#         x = len(nums2[:mid2]) + len(nums1[:mid1-1])
#         if x == len(nums1)+len(nums2) or x == len(nums1)+len(nums2)-1:
#             sum += mid1
#     if mid2 > mid1:
#         x = len(nums1[:mid1]) + len(nums2[:mid2-1])
#         if x == len(nums2)+len(nums1) or x == len(nums2)+len(nums1)-1:
#             sum += mid2
#     return sum/2

def findmedian(nums1, nums2):
    if len(nums1) == 1 and len(nums2) == 1:
        return ((nums1[0]+nums2[0])/2)
    i = 0
    j = 0
    lst = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            lst.append(nums1[i])
            i += 1
        else:
            lst.append(nums2[j])
            j += 1
        if i < len(nums1):
            lst = lst + nums1[i:]
        if j < len(nums2):
            lst = lst + nums2[j:]
        l = len(lst)
        if l % 2 == 1:
            return lst[l//2]
        else:
            return ((lst[l//2]+lst[(l//2)-1])/2)


print(findmedian([1, 2], [3, 4]))
print(findmedian([1, 3, 4, 7, 11], [3, 6, 8, 9, 10]))
