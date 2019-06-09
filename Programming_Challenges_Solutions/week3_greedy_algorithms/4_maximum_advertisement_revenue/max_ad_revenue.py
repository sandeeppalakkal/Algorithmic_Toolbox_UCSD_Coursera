# Uses Python3
'''Maximum Advertisement Revenue
Problem Introduction
You have 𝑛 ads to place on a popular Internet page. For each ad, you know how
much is the advertiser willing to pay for one click on this ad. You have set up 𝑛
slots on your page and estimated the expected number of clicks per day for each
slot. Now, your goal is to distribute the ads among the slots to maximize the
total revenue.
Problem Description
Task. Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is
        the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗)
such that the sum of their products is maximized.
Input Format. The first line contains an integer 𝑛, the second one contains a sequence of integers
𝑎1, 𝑎2, . . . , 𝑎𝑛, the third one contains a sequence of integers 𝑏1, 𝑏2, . . . , 𝑏𝑛.
Constraints. 1 ≤ 𝑛 ≤ 1e3; −1e5 ≤ 𝑎𝑖, 𝑏𝑖 ≤ 1e5 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format. Output the maximum value of
Σ︀𝑛
𝑖=1
𝑎𝑖𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of
𝑏1, 𝑏2, . . . , 𝑏𝑛.'''

import numpy as np

def check_order(a,b,mode = 'ASC'):
    '''Check order of a & b: if ascending (b>a) or descending (b<a)'''
    if mode == 'ASC':
        return not b == min(a,b)
    elif mode == 'DESC':
        return not b == max(a,b)

def arrange_around_pivot(a,p,i,j,order):
    k = i
    while i < j and k <= j:
        if check_order(a[k],p,order):
            t = a[i]
            a[i] = a[k]
            a[k] = t
            i += 1
            k += 1
        elif check_order(p,a[k],order):
            t = a[j]
            a[j] = a[k]
            j -= 1
            a[k] = t
        else:
            k += 1
    return i

def quick_sort(a,i,j,order='ASC'):
    if i >= j:
        return
    p = a[i]
    pi = arrange_around_pivot(a,p,i,j,order)
    quick_sort(a,i,pi-1,order)
    quick_sort(a,pi+1,j,order)
    return

def sort(a,order='ASC'):
    #quick_sort(a,0,len(a)-1,order)
    a = np.sort(a)
    return a

def linear_sum(a,b):
    assert len(a) == len(b)
    c = 0
    for i,j in zip(a,b):
        c += i*j
    return c

def max_revenue(a,b):
    a = sort(a,'DESC')
    b = sort(b,'DESC')
    p = linear_sum(a,b)
    return p

def main():
    n = int(input())
    a = np.array([int(x) for x in input().split()[:n]],dtype=np.int64)
    b = np.array(list(map(int,input().split()[:n])),dtype=np.int64)
    p = max_revenue(a,b)
    print(p)

if __name__ == '__main__':
    main()
