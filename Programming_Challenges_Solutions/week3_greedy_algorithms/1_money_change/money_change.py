# Uses Python3
'''In this problem, you will design and implement an elementary greedy algorithm
used by cashiers all over the world millions of times per day.'''

'''Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer 𝑚.
Constraints. 1 ≤ 𝑚 ≤ 103.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.'''

def compute_changes(total,denoms):
    n_denoms = len(denoms)
    changes = [0] * n_denoms
    i = n_denoms - 1
    while total != 0:
        changes[i] = total // denoms[i]
        total %= denoms[i]
        i -= 1
    return changes
        
def main():
    total = int(input())
    denoms = [1,5,10]
    changes = compute_changes(total,denoms)
    n_coins = sum(changes)
    print(n_coins)

if __name__ == '__main__':
    main()
