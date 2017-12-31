# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """knapsack problem:
    get the optimal fractional configuration of values/weights that fills
    the capacity.
    """
    assert len(weights) == len(values)

    value = 0.
    weights_values = list(zip(weights, values))
    weights_values.sort(key=lambda x: x[1] / x[0], reverse=True)
    while capacity and len(weights_values) > 0:
        w, v = weights_values[0]
        if capacity >= w:
            value += v
            capacity -= w
        else:
            value += capacity * v / w
            capacity = 0
        weights_values.pop(0)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
