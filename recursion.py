def findmax(xs):
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return xs[0]
    if len(xs) == 2:
        if xs[0] < xs[1]:
            return xs[1]
        else:
            return xs[0]
    mid = len(xs)//2
    first_half_greatest = findmax(xs[:mid])
    sec_half_greatest = findmax(xs[mid:])
    return findmax([first_half_greatest, sec_half_greatest])


xs = [120, 34, 54, 32, 58, 11, 90]
print(xs[0:1])

# def findmin(xs):
#     if len(xs) == 0:
#         return []
#     if len(xs) == 1:
#         return xs[0]
#     if len(xs) == 2:
#         if xs[0] < xs[1]:
#             return xs[0]
#         else:
#             return xs[1]
#     mid = len(xs)//2
#     first_half_min = findmin(xs[:mid])
#     sec_half_min = findmin(xs[mid:])
#     return findmin([first_half_min, sec_half_min])


# def merge(xs, ys):
#     lst = []
#     i = 0
#     j = 0
#     while i < len(xs) and j < len(ys):
#         if xs[i] > ys[j]:
#             lst.append(ys[j])
#             j += 1
#         elif xs[i] < ys[j]:
#             lst.append(xs[i])
#             i += 1
#     if j < len(ys):
#         return lst+ys[j:]
#     if i < len(xs):
#         return lst+xs[i:]
#     return lst


# def mergesort(xs):
#     if len(xs) == 0:
#         return []
#     if len(xs) == 1:
#         return xs
#     if len(xs) == 2:
#         if xs[0] > xs[1]:
#             temp = xs[0]
#             xs[0] = xs[1]
#             xs[1] = temp
#             return xs
#         else:
#             return xs
#     mid = len(xs)//2
#     first_half = mergesort(xs[:mid])
#     sec_half = mergesort(xs[mid:])
#     return merge(first_half, sec_half)


# def partition(xs, start, end):
#     pivot = xs[end]
#     lo = start
#     hi = end-1
#     while True:
#         while lo != hi and xs[lo] <= pivot:
#             lo += 1
#         while lo != hi and xs[hi] >= pivot:
#             hi -= 1
#         if lo != hi:
#             temp = xs[lo]
#             xs[lo] = xs[hi]
#             xs[hi] = temp
#         else:
#             break
#     if xs[hi] < pivot:
#         return hi+1
#     xs[end] = xs[hi]
#     xs[hi] = pivot
#     return hi


# def quicksort(xs, start, end):
#     if start >= end:
#         return
#     part = partition(xs, start, end)
#     quicksort(xs, start, part-1)
#     quicksort(xs, part+1, end)
#     return xs


# test = [8, 10, 7, 9, 1, 5]
# xs = [12, 13, 11, 5, 6, 7]
# ys = [12, 1, 4, 3, 5, 6, 7, 8, 43]
# lst = [70, 250, 50, 80, 140, 12, 14]
# ys = [120, 34, 54, 32, 58, 11, 90]
# assert quicksort(test, 0, len(test)-1) == [1, 5, 7, 8, 9, 10]
# findmax(lst)
# findmax(ys)

# can we do partition recursively
# challange for each of the functions that you wrote give an argument for the complexity
# can we do bubblesort recursively ?
# is it possible to do paritition recursively
# what is the complexity of partition?
