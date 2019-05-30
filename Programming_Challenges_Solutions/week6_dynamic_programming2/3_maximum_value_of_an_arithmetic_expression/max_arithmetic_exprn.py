# Uses Python3
'''Maximum Value of an Arithmetic Expression
Problem Introduction
In this problem, your goal is to add parentheses to a given arithmetic
expression to maximize its value. max(5−8+7×4−8+9) =?
Problem Description
Task. Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
operations using additional parentheses.
Input Format. The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols
𝑠0, 𝑠1, . . . , 𝑠2𝑛. Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while
each symbol at an odd position is one of three operations from {+,-,*}.
Constraints. 1 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).
Output Format. Output the maximum possible value of the given arithmetic expression among different
orders of applying arithmetic operations.'''

import numpy as np

def evaluate(a,b,op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op in ['*','x']:
        return a * b

def min_and_max(M,m,op,i,j):
    min_ = None
    max_ = None
    for k in range(i,j):
        a = evaluate(M[i,k],M[k+1,j],op[k])
        b = evaluate(M[i,k],m[k+1,j],op[k])
        c = evaluate(m[i,k],M[k+1,j],op[k])
        d = evaluate(m[i,k],m[k+1,j],op[k])
        if min_ == None and max_ == None:
            min_ = min(a,b,c,d)
            max_ = max(a,b,c,d)
        else:
            min_ = min(min_,a,b,c,d)
            max_ = max(max_,a,b,c,d)
    return (min_,max_)

def max_arithmetic_expression(e):
    d = e[::2]
    o = e[1::2]
    n = len(d)
    M = np.zeros((n,n),dtype=int)
    m = np.zeros((n,n),dtype=int)
    for i in range(n):
        m[i,i] = d[i]
        M[i,i] = d[i]
    for s in range(1,n):
        for i in range(0,n-s):
            j = i + s
            m[i,j],M[i,j] = min_and_max(M,m,o,i,j)
    #print(m)
    #print(M)
    return M[0,n-1]

def main():
    e = str(input())
    assert(len(e) % 2 == 1)
    max_val = max_arithmetic_expression(e)
    print(max_val)

if __name__ == '__main__':
    main()
