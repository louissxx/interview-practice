def qs_first(xs):
    """
    xs: list
    The function sorts xs in place (using deterministic pivots) and returns the
    number of comparisons that were performed 
    """
    pivot = xs[0]
    lo = 1
    hi = len(xs)-1
    count = 0
    while True:
        while lo != hi and xs[lo] <= pivot:
            lo += 1
            count += 1
        while lo != hi and xs[hi] >= pivot:
            hi -= 1
            count += 1
        if lo != hi:
            temp = xs[lo]
            xs[lo] = xs[hi]
            xs[hi] = temp
            count += 2
        else:
            break
    xs[0] = xs[hi-1]
    xs[hi-1] = pivot
    return count


xs = [8, 10, 7, 9, 1, 5]
print(qs_first(xs))


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


# xs = [8, 10, 7, 9, 1, 5]
# ys = [5, 1, 7, 2, 4]
# test = [5, 7, 9, 8, 10]
# final = [5, 7, 9, 8]


# assert partition(xs, 0, len(xs)-1) == (1)
# assert partition(ys, 0, len(ys)-1) == (2)
# assert partition(test, 0, len(test)-1) == (4)
# assert partition(final, 0, len(final)-1) == (2)


#  def partition(xs, start, end):
#     pivot = xs
#     end_pointer = end
#     start_pointer = start + 1
#     while True:
#         while start_pointer <= end_pointer and xs[end_pointer] >= pivot:
#             end_pointer -= 1
#         while start_pointer <= end_pointer and xs[start_pointer] <= pivot:
#             start_pointer += 1

#         if start_pointer <= end_pointer:
#             temp = xs[start_pointer]
#             xs[start_pointer] = xs[end_pointer]
#             xs[end_pointer] = temp
#         else:
#             break

#     temp = xs[start]
#     xs[start] = xs[end_pointer]
#     xs[end_pointer] = temp
#     return end_pointer


# def partition(xs, start, end):
#     pivot = xs[-1]
#     end_pointer = end-1
#     start_pointer = start
#     run_end = False
#     while start_pointer <= end_pointer:
#         if xs[start_pointer] < pivot and start_pointer <= end_pointer:
#             start_pointer += 1
#         else:
#             run_end = True
#             if xs[end_pointer] > pivot and start_pointer <= end_pointer:
#                 end_pointer -= 1
#             else:
#                 temp = xs[start_pointer]
#                 xs[start_pointer] = xs[end_pointer]
#                 xs[end_pointer] = temp
#     if run_end:
#         xs[-1] = xs[end_pointer]
#         xs[end_pointer] = pivot
#     else:
#         if xs[end_pointer] < pivot:
#             return end_pointer+1
#         else:
#             xs[-1] = xs[end_pointer]
#             xs[end_pointer] = pivot
#     return end_pointer


# def partition(xs, start, end):
#     pivot = xs[start]
#     end_pointer = end
#     start_pointer = start + 1
#     while True:
#         while start_pointer <= end_pointer and xs[end_pointer] >= pivot:
#             end_pointer -= 1
#         while start_pointer <= end_pointer and xs[start_pointer] <= pivot:
#             start_pointer += 1

#         if start_pointer <= end_pointer:
#             temp = xs[start_pointer]
#             xs[start_pointer] = xs[end_pointer]
#             xs[end_pointer] = temp
#         else:
#             break

#     temp = xs[start]
#     xs[start] = xs[end_pointer]
#     xs[end_pointer] = temp
#     return end_pointer
