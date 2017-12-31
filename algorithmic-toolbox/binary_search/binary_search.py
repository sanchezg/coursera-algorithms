# Uses python3
import sys


def binary_search(a, x):
    low, high = 0, len(a) - 1
    found = False
    candidate = -1
    # a.sort()
    while low <= high and not found:
        mid = (low + high) // 2
        if (x == a[mid]):
            candidate = mid
            found = True
        elif (x < a[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return candidate


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
