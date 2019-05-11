# Uses Python3
'''Last digit of F(n) (i.e., F(n) mod 10) will be 
   the last digit of sum of last digits of  F(n-1) and F(n-2).
   So, we need to only keep the last digit of F(k) k < n during 
   the iterative computation. This can be done by taking mod 10'''

import time
import numpy as np

# Fastest O(n)
def fibonacci_iterative_last_digit(n):
    if n in [0,1]: return n

    fn_1 = 1
    fn_2 = 0

    for n in range(2,n+1):
        temp = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = temp % 10

    return fn_1

def main():
    n = int(input())
    assert n >= 0
    start_time = time.time()
    fn_d = fibonacci_iterative_last_digit(n)
    end_time = time.time()
    print(fn_d)
    #print(end_time - start_time)

if __name__ == '__main__':
    main()
