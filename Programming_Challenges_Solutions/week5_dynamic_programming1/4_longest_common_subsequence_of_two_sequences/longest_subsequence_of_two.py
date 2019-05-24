# Uses Python3
'''Longest Common Subsequence of Two Sequences
Problem Introduction
Compute the length of a longest common subsequence of three sequences.
Problem Description
Task. Given two sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛) and 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), find the length of their longest
common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices 1 ≤ 𝑖1 <
𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛 and 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, such that 𝑎𝑖1 = 𝑏𝑗1 , . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝 .
Input Format. First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚.
Constraints. 1 ≤ 𝑛,𝑚 ≤ 100; −1e9 < 𝑎𝑖, 𝑏𝑖 < 1e9.
Output Format. Output 𝑝.'''

import numpy as np
import copy

def compute_edit_distance_matrix_DP(str1,str2):
    n = len(str1)
    m = len(str2)
    D = np.zeros((n+1,m+1))
    D[0,:] = np.arange(m+1)
    D[:,0] = np.arange(n+1)
    for j in range(0,m):
        for i in range(0,n):
            ins_dist = D[i+1,j] + 1
            del_dist = D[i,j+1] + 1
            match_dist = D[i,j]
            mismatch_dist = D[i,j] + 2
            if str1[i] == str2[j]:
                D[i+1,j+1] = min(ins_dist,del_dist,match_dist)
            else:
                D[i+1,j+1] = min(ins_dist,del_dist,mismatch_dist)
    return D

def matches(D):
    n,m = D.shape
    j = m - 1
    i = n - 1
    p = 0
    while i > 0 and j > 0:
        if D[i-1,j-1] == D[i,j]:
            p += 1
        i -= 1
        j -= 1
    return p

def max_subseq_len(str1,str2):
    D = compute_edit_distance_matrix_DP(str1,str2)
    #print(D)
    p = matches(D)
    return p

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    d = max_subseq_len(a,b)
    print(d)

if __name__ == '__main__':
    main()
