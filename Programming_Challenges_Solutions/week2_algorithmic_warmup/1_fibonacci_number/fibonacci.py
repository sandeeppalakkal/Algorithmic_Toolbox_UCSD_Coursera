# Uses Python3
import time
import numpy as np

# The fastest O(1)
def fibonacci_formula(n):
    phi = 0.5 * (np.sqrt(5) + 1)
    psi = 1 - phi
    #fn = round((phi**n - psi**n)/sqrt(5))
    fn = int(np.round(phi ** n / np.sqrt(5)))
    return fn

# Fastest O(n)
def fibonacci_iterative(n):
    if n in [0,1]: return n

    fn_1 = 1
    fn_2 = 0

    for n in range(2,n+1):
        temp = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = temp

    return fn_1

def fibonacci_memoized_recursion(n,fib_array):
    if n in [0,1]: return
    if fib_array[n] == 0:
        if fib_array[n-1] == 0:
            fibonacci_memoized_recursion(n-1,fib_array)    
        if fib_array[n-2] == 0:
            fibonacci_memoized_recursion(n-2,fib_array)    
        fib_array[n] = fib_array[n-1] + fib_array[n-2]
    return

def fibonacci_memoisation(n):
    if n in [0,1]: return n
    
    fib_array = [0]*(n+1)
    fib_array[1] = 1

    fibonacci_memoized_recursion(n,fib_array)

    return fib_array[n]


def fibonacci_recursive(n):
    if n in [0,1]:
        return n
    elif n > 1:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def main():
    n = int(input())
    assert n >= 0
    start_time = time.time()
    #fn = fibonacci_recursive(n)
    fn = fibonacci_iterative(n)
    #fn = fibonacci_memoisation(n)
    #fn = fibonacci_formula(n)
    end_time = time.time()
    print(fn)
    #print(end_time - start_time)

if __name__ == '__main__':
    main()
