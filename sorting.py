def bubblesort(xs):
    i = 0
    while i < len(xs)-1:
        if xs[i] > xs[i+1]:
            temp = xs[i]
            xs[i] = xs[i+1]
            xs[i+1] = temp
            i = 0
        else:
            i += 1
    return xs


def bubblesort2(xs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if xs[i] < xs[j]:
                temp = xs[i]
                xs[i] = xs[j]
                xs[j] = temp
    return xs


def bubblesortrec(xs):
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return xs
    for i in range(len(xs)-1):
        if xs[i] > xs[i+1]:
            temp = xs[i]
            xs[i] = xs[i+1]
            xs[i+1] = temp
            bubblesortrec(xs)


# xs = [10, 12, 5, 1, 4, 2, 9, 7, 8]
# bubblesortrec(xs)
# print(xs)


def insert(xs, i, x):
    temp = xs[i]
    xs[i] = x
    if i < len(xs)-1:
        insert(xs, i+1, temp)
    if i == len(xs)-1:
        xs.append(temp)
    return xs


# xs = [1, 2, 3, 4]
# assert insert(xs, 2, 5) == [1, 2, 5, 3, 4]
# lst = [6, 2, 1, 4]

# vowel = ['a', 'e', 'i', 'u']
# assert insert(vowel, 3, 'o') == ['a', 'e', 'i', 'o', 'u']

# test = [2, 3, 4, 5, 6]
# assert insert(test, 0, 1) == [1, 2, 3, 4, 5, 6]

# xs = [7, 5, 8, 4, 3, 1]
# assert insert(xs, 0, 2) == [2, 7, 5, 8, 4, 3, 1]


def insertionsort(xs):
    for i in range(1, len(xs)):
        for j in range(0, i):
            if xs[i] < xs[j]:
                insert(xs, j, xs[i])
                xs.pop(i+1)
    return xs


# xs = [5, 4, 3, 7, 8, 10, 5, 4, 6, 1]
# ys = [1, 1, 1, 1, 1, 1, 0]
# wabble = [1, 2, 3, 4, 3, 2, 1]
# lst = [1]
# lst2 = [2, 1]
# lst3 = [1, 1, 1]
# assert insertionsort(xs) == [1, 3, 4, 4, 5, 5, 6, 7, 8, 10]
# assert insertionsort(ys) == [0, 1, 1, 1, 1, 1, 1]
# assert insertionsort(wabble) == [1, 1, 2, 2, 3, 3, 4]
# assert insertionsort(lst) == [1]
# assert insertionsort(lst2) == [1, 2]
# assert insertionsort(lst3) == [1, 1, 1]


def findmin(xs):
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return xs[0]
    if len(xs) == 2:
        if xs[0] < xs[1]:
            return xs[0]
        else:
            return xs[1]
    mid = len(xs)//2
    first_half_min = findmin(xs[:mid])
    sec_half_min = findmin(xs[mid:])
    return findmin([first_half_min, sec_half_min])


def minindex(xs):
    min = xs[0]
    result = 0
    i = 1
    while i < len(xs):
        if xs[i] < min:
            min = xs[i]
            result = i
        i += 1
    return result


def selectionsort(xs):
    i = 0
    while i < len(xs)-1:
        mi = minindex(xs[i:])
        actual = mi+i
        temp = xs[i]
        xs[i] = xs[actual]
        xs[actual] = temp
        i += 1
    return xs


xs = [5, 7, 2, 1, -5]
ys = [5, 4, 3, 2, 1, 0]
selectionsort(ys)
print(ys)
