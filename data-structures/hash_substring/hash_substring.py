# python3
import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def get_bigprime():
    return 1610612741


def poly_hash(text, p, x):
    h = 0
    for c in reversed(text):
        h = (h * x + ord(c)) % p
    return h


def precompute_hashes(text, pattern_len, p, x):
    hashes = [None] * (len(text) - pattern_len + 1)
    s = text[len(text) - pattern_len:]
    hashes[len(text) - pattern_len] = poly_hash(s, p, x)
    y = 1
    for i in range(pattern_len):
        y = (y * x) % p
    for i in range(len(text) - pattern_len - 1, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) -
                     y * ord(text[i + pattern_len])) % p
    return hashes


def get_occurrences_rabinkarp(pattern, text):
    p = get_bigprime()
    x = random.randint(1, p - 1)
    result = []
    p_hash = poly_hash(pattern, p, x)
    pattern_len = len(pattern)
    hashes = precompute_hashes(text, pattern_len, p, x)
    for i in range(len(text) - pattern_len + 1):
        if p_hash == hashes[i] and text[i:i + pattern_len] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences_rabinkarp(*read_input()))
