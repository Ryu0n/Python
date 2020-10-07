from bisect import bisect_left, bisect_right

def binarySearch(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)

def binarySearch2(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

def count_by_range(a, lvalue, rvalue):
    lIndex = bisect_left(a, lvalue)
    rIndex = bisect_right(a, rvalue)
    print(lIndex, rIndex)
    return rIndex - lIndex

a = [1, 2, 4, 4, 8]
b = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
x = 3

print(bisect_left(a, x))
print(bisect_right(a, x))

print(count_by_range(b, -1, 4))