"""
O(n)
"""


def linearSearch(array, search):
    array.sort()
    for i, num in enumerate(array):
        if num == search:
            return True
    else:
        return False


"""
O(log n)
"""


def binarySearch(array, search):
    array.sort()
    first = 0
    last = len(array) - 1
    middle = (first + last) // 2

    while first <= last:
        if array[middle] < search:
            first = middle + 1
        elif array[middle] == search:
            return True
        else:
            last = middle - 1
        middle = (first + last) // 2

    if first > last:
        return False


"""
O(log n)
"""


def ternarySearch(array, search):
    array.sort()
    (left, right) = (0, len(array) - 1)
    while left <= right:
        leftMid = left + (right - left) // 3
        rightMid = right - (right - left) // 3

        if array[leftMid] == search:
            return True
        elif array[rightMid] == search:
            return True
        elif array[leftMid] > search:
            right = leftMid - 1
        elif array[rightMid] < search:
            left = rightMid + 1
        else:
            left = leftMid + 1
            right = rightMid - 1

    return False
