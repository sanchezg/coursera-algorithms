# Uses python3
import sys


def get_change(m):
    """Returns the minimum number of coins that exchanges the input money m.
    Coins denomination: [10, 5, 1]
    For example:
        Input: 2
        Ouput: 2 = 1+1

        Input: 28
        Ouput: 6 = 10+10+5+1+1
    """
    coins = [10, 5, 1]
    amount = 0
    while m:
        selected = coins[0]
        if m - selected >= 0:
            amount += 1
            m -= selected
            # if m == 0, ends loop
        else:
            # m - selected < 0
            coins.pop(0)
    return amount


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
