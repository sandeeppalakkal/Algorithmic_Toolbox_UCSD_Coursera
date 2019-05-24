# Uses Python3
'''Money Change Again
As we already know, a natural greedy strategy for the change problem does not work correctly for any set of
denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change
6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is
to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.
Problem Description
Input Format. Integer money.
Output Format. The minimum number of coins with denominations 1, 3, 4 that changes money.
Constraints. 1 ≤ money ≤ 1e3.'''

def money_changes(m,coins):
    change_array = [-1] * (m + 1)
    change_array[0] = 0
    # Run for all money from 0 to m:
    for i in range(1,m+1):
        # DP Step:
        # Run for all coins & compute min changes:
        min_change = m
        for c in coins:
            if i < c:
                break
            # DP Formula:
            change = change_array[i-c] + 1
            if change < min_change:
                min_change = change
        change_array[i] = min_change
    return change_array[m]


def main():
    coins = [1,3,4]
    m = int(input())
    n = money_changes(m,coins)
    print(n)

if __name__ == '__main__':
    main()
