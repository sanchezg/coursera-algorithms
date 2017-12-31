# Uses python3
import sys


def is_greater_or_equal_than(digit, max_digit):
    return int(digit + max_digit) >= int(max_digit + digit)


def largest_number(digits):
    """Compose the largest number out of a set of integers.
    """
    res = ""
    while digits:
        max_digit = None
        for digit in digits:
            if max_digit is None or \
               is_greater_or_equal_than(digit, max_digit):
                max_digit = digit
        res += max_digit
        digits.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
