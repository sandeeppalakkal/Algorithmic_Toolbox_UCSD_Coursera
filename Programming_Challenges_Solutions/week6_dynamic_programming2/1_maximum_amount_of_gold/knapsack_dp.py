# Uses Python3
'''Maximum Amount of Gold
Problem Introduction
You are given a set of bars of gold and your goal is to take as much gold as possible into
your bag. There is just one copy of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar).
Problem Description
Task. Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.
Input Format. The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars
of gold. The next line contains 𝑛 integers 𝑤0,𝑤1, . . . ,𝑤𝑛−1 defining the weights of the bars of gold.
Constraints. 1 ≤ 𝑊 ≤ 1e4; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . ,𝑤𝑛−1 ≤ 1e5.
Output Format. Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.'''

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

def main():
    knap_w,n = [int(x) for x in input().split()[:2]]
    w = [int(x) for x in input().split()[:n]]
    max_w,items = max_weight_knapsack(knap_w,w)
    print(max_w)
    #print(items)

if __name__ == '__main__':
    main()
