# Uses Python3
'''Majority Element
Problem Introduction
Majority rule is a decision rule that selects the alternative which has a majority,
 that is, more than half the votes.
 Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to check whether
 it contains an element that appears more than 𝑛/2 times. A naive way to do
 this is the following.
    MajorityElement(𝑎1, 𝑎2, . . . , 𝑎𝑛):
    for 𝑖 from 1 to 𝑛:
    currentElement ← 𝑎𝑖
    count ← 0
    for 𝑗 from 1 to 𝑛:
    if 𝑎𝑗 = currentElement:
    count ← count + 1
    if count > 𝑛/2:
    return 𝑎𝑖
    return “no majority element”
The running time of this algorithm is quadratic. Your goal is to use the divide-and-conquer technique to
design an 𝑂(𝑛 log 𝑛) algorithm.
Problem Description
Task. The goal in this code problem is to check whether an input sequence contains a majority element.
Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints. 1 ≤ 𝑛 ≤ 105; 0 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.
Output Format. Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
and 0 otherwise.'''

import time

def majority_element_naive(a):
    n = len(a)
    for i in range(n//2):
        ni = 1
        for j in range(i+1,n):
            if a[j] == a[i]: 
                ni += 1
        if ni > (n-i)//2:
            return a[i],ni
    return 0,0

def get_count(a,e):
    n = 0
    for i in range(len(a)):
        if a[i] == e:
            n += 1
    return n

def majority_element(a):
    n = len(a)
    #if n <=3:
    #    maj,n_maj = majority_element_naive(a)
    #    return maj,n_maj
    if n == 1: return a[0],1
    elif n == 2:
        if a[0] == a[1]: return a[0],2
    left_maj,nl = majority_element(a[:n//2])
    right_maj,nr = majority_element(a[n//2:])
    linr = get_count(a[n//2:],left_maj)
    if nl + linr > n//2:
        return left_maj,nl+linr
    rinl = get_count(a[:n//2],right_maj)
    if nr + rinl > n//2:
        return right_maj, nr+rinl
    return 0,0

def main():
    n = int(input())
    a = list(map(int,input().split()))
    #t1 = time.time()
    #e,_ = majority_element_naive(a)
    #t2 = time.time()
    #print(e)
    #print(t2-t1)
    #t1 = time.time()
    e,_ = majority_element(a)
    #t2 = time.time()
    print(int(e != 0))
    #print(t2-t1)

if __name__ == '__main__':
    main()
