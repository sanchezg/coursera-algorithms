# Uses python3
import sys


def optimal_weight(W, weights):
    partial_results = [[0 for i in range(W + 1)] for j in range(len(weights) + 1)]
    # weights.sort()
    # import ipdb; ipdb.set_trace()
    for i in range(1, len(weights) + 1):
        for j in range(1, W + 1):
            partial_results[i][j] = partial_results[i - 1][j]
            if weights[i - 1] > j:
                continue
            # for each bar, its value is the same as weight
            candidate = partial_results[i - 1][j - weights[i - 1]] + weights[i - 1]
            partial_results[i][j] = max(candidate, partial_results[i][j])
    return partial_results[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
