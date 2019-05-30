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

def compute_match_matrix(a,b):
    n = len(a)
    m = len(b)
    D = np.zeros((n+1,m+1))
    for j in range(0,m):
        for i in range(0,n):
            if a[i] == b[j]:
                D[i+1,j+1] = D[i,j] + 1
            else:
                D[i+1,j+1] = max(D[i+1,j],D[i,j+1])
    return D

def max_subseq_len(a,b):
    D = compute_match_matrix(a,b)
    #print(D)
    return int(D[-1,-1])

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    d = max_subseq_len(a,b)
    print(d)

if __name__ == '__main__':
    main()
