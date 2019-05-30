# Uses Python3
'''Edit Distance
Problem Introduction
The edit distance between two strings is the minimum number of operations (insertions, deletions, and
        substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance between two strings.
Problem Description
Task. The goal of this problem is to implement the algorithm for computing the edit distance between two
strings.
Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters.
Constraints. The length of both strings is at least 1 and at most 100.
Output Format. Output the edit distance between the given two strings.'''

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
            mismatch_dist = D[i,j] + 1
            if str1[i] == str2[j]:
                D[i+1,j+1] = min(ins_dist,del_dist,match_dist)
            else:
                D[i+1,j+1] = min(ins_dist,del_dist,mismatch_dist)
    return D

# Backtrack
def backtrack(D,i,j):
    if i < 0 or j < 0:
        return 'n'
    if i == 0 and j == 0:
        return 's'
    if i == 0:
        return 'i'
    if j == 0:
        return 'd'
    if D[i-1,j-1] <= D[i,j]:
        return 'm'
    if D[i-1,j] < D[i,j]:
        return 'd'
    if D[i,j-1] < D[i,j]:
        return 'i'
    return 'n'

# Recursive function
def output_alignment(str1,str2,D,i,j):
    if i <= 0 and j <= 0:
        return str1,str2
    step_back = backtrack(D,i,j)
    assert step_back != 'n'
    if step_back == 's':
        return str1,str2
    if step_back == 'i':
        str1,str2 = output_alignment(str1,str2,D,i,j-1)
        str1 = str1[:i] + '_' + str1[i:]
        return str1,str2
    if step_back == 'd':
        str1,str2 = output_alignment(str1,str2,D,i-1,j)
        str2 = str2[:j] + '_' + str2[j:]
        return str1,str2
    if step_back == 'm':
        str1,str2 = output_alignment(str1,str2,D,i-1,j-1)
        return str1,str2

def construct_edit_outputs(str1,str2,D):
    n = len(str1)
    m = len(str2)
    str1_,str2_ = output_alignment(str1,str2,D,n,m)
    return str1_,str2_ 

def edit_distance(str1,str2):
    D = compute_edit_distance_matrix_DP(str1,str2)
    print(D)
    str1_,str2_ = construct_edit_outputs(str1,str2,D)
    #print(str1_)
    #print(str2_)
    return int(D[-1,-1])

def main():
    str1 = input()
    str2 = input()
    d = edit_distance(str1,str2)
    print(d)

if __name__ == '__main__':
    main()
