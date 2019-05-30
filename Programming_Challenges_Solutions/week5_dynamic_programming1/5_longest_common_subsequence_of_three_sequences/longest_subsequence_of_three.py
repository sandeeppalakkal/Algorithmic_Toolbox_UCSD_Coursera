# Uses Python3
'''Longest Common Subsequence of Three Sequences
Problem Introduction
Compute the length of a longest common subsequence of three sequences.
Problem Description
Task. Given three sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛), 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), and 𝐶 = (𝑐1, 𝑐2, . . . , 𝑐𝑙), find the
length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there
exist indices 1 ≤ 𝑖1 < 𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛, 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, 1 ≤ 𝑘1 < 𝑘2 < · · · < 𝑘𝑝 ≤ 𝑙 such
that 𝑎𝑖1 = 𝑏𝑗1 = 𝑐𝑘1 , . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝 = 𝑐𝑘𝑝
Input Format. First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚. Fifth line:
𝑙. Sixth line: 𝑐1, 𝑐2, . . . , 𝑐𝑙.
Constraints. 1 ≤ 𝑛, 𝑚, 𝑙 ≤ 100; −1e9 < 𝑎𝑖, 𝑏𝑖, 𝑐𝑖 < 1e9.
Output Format. Output 𝑝.'''

import numpy as np
import copy

def compute_match_matrix(a,b,c):
    n = len(a)
    m = len(b)
    l = len(c)
    D = np.zeros((n+1,m+1,l+1))
    for k in range(0,l):
        for j in range(0,m):
            for i in range(0,n):
                if a[i] == b[j] == c[k]:
                    D[i+1,j+1,k+1] = D[i,j,k] + 1
                else:
                    D[i+1,j+1,k+1] = max(D[i+1,j,k],D[i+1,j+1,k],
                                         D[i,j+1,k+1],D[i+1,j,k+1],
                                         D[i,j+1,k],D[i,j,k+1])
    return D

def max_subseq_len(a,b,c):
    D = compute_match_matrix(a,b,c)
    #print(D)
    return int(D[-1,-1,-1])

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    l = int(input())
    c = [int(x) for x in input().split()]
    d = max_subseq_len(a,b,c)
    print(d)

if __name__ == '__main__':
    main()
