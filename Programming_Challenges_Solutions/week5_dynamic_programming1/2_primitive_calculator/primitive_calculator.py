# Uses Python3
'''Problem Introduction
You are given a primitive calculator that can perform the following three operations with
the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a
positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.
Problem Description
Task. Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.
Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 1e6.
Output Format. In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1.
In the second line output a sequence of intermediate numbers. That is, the second line should contain
positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎𝑖+1 is equal to
either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. If there are many such sequences, output any one of them.'''

import time

def intermediate_operation(x,op):
    if op == 1:
        return x-1
    elif op == 2:
        x = x / 2
        if x == int(x):
            return int(x)
        else:
            return -1
    elif op == 3:
        x = x / 3
        if x == int(x):
            return int(x)
        else:
            return -1

def calculator_outputs_dp(n):
    ops_array = [0] * (n+1)
    intermediate_output = [[]] * (n+1)
    intermediate_output[1] = [1]
    for num in range(2,n+1):
        min_ops = n
        intermediate = -1
        for op in range(1,4):
            k = intermediate_operation(num,op)
            if k != -1:
                ops = ops_array[k] + 1
                if ops <= min_ops:
                    min_ops = ops
                    intermediate = k
        ops_array[num] = min_ops
        intermediate_output[num] = intermediate_output[intermediate] + [num]
    return intermediate_output[n]
    
# Greedy produces wrong result for this problem
def calculator_outputs_greedy(n):
    op_counts = 0
    intermediate = []
    while n > 0:
        intermediate.append(n)
        n3 = n / 3
        n2 = n / 2
        n1 = n - 1
        if n3 == int(n3):
            n = int(n3)
        elif n2 == int(n2):
            n = int(n2)
        else:
            n = n1
    intermediate = intermediate[::-1]
    return intermediate

def print_results(outputs):
    n_ops = len(outputs)-1
    print(n_ops)
    for o in outputs:
        print(o,end = " ")
    print()
        
def main():
    n = int(input())
    t1 = time.time()
    # DP is the correct approach
    outputs = calculator_outputs_dp(n)
    print_results(outputs)
    t2 = time.time()
    # Greedy produces wrong result for this problem
    #outputs = calculator_outputs_greedy(n)
    #print_results(outputs)
    #t3 = time.time()
    #print(t2-t1)
    #print(t3-t2)

if __name__ == '__main__':
    main()
