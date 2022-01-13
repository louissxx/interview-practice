def binarysearch(xs, target):
    lo = 0
    hi = len(xs)
    while lo != hi:
        mid = (lo+hi)//2
        if xs[mid] == target:
            return mid
        elif xs[mid] < target:
            lo = mid+1
        elif xs[mid] > target:
            hi = mid
    return -1
