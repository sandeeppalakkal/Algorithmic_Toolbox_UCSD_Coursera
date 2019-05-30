# Uses Python3

'''Partitioning Souvenirs
You and two of your friends have just returned back home after visiting various countries. Now you would
like to evenly split all the souvenirs that all three of you bought.
Problem Description
Input Format. The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated
by spaces.
Constraints. 1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣𝑖 ≤ 30 for all 𝑖.
Output Format. Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and
0 otherwise.'''

import numpy as np

def max_weight_knapsack(knap_w,w):
    n = len(w)
    val_arr = np.zeros((n+1,knap_w+1),dtype=int)
    include_list = [[] for i in range((n+1))]
    for j in range(n+1):
        include_list[j] = [[] for i in range(knap_w + 1)]
    for ni in range(1,n+1):
        for wi in range(1,knap_w+1):
            # Value if ni is not included for current max capacity
            val_arr[ni,wi] = val_arr[ni-1,wi]
            include_list[ni][wi] = include_list[ni-1][wi]
            if w[ni-1] <= wi:
                # Value if ni is included for current max capacity
                val = val_arr[ni-1,wi-w[ni-1]] + w[ni-1]
                # Chose the best
                if val > val_arr[ni,wi]:
                    val_arr[ni,wi] = val
                    include_list[ni][wi] = include_list[ni-1][wi-w[ni-1]] + [ni]
    #print(val_arr)
    #for lst in include_list:
    #    print(lst)
    return val_arr[n,knap_w],include_list[-1][-1]


def equal_partition(v):
    total = sum(v)
    if total % 3 != 0:
        return 0
    indiv_val = total // 3
    for i in range(3):
        amt,items = max_weight_knapsack(indiv_val,v)
        #print(amt)
        if amt != indiv_val:
            return 0
        # since items is sorted:
        for j,ind in enumerate(items):
            # update index as j are already removed
            t = v.pop(ind - 1 - j)
            print(t,end=', ')
        print()
    return 1

def main():
    n = int(input())
    v = [int(x) for x in input().split()[:n]]
    flag = equal_partition(v)
    print(flag)

if __name__ == '__main__':
    main()
