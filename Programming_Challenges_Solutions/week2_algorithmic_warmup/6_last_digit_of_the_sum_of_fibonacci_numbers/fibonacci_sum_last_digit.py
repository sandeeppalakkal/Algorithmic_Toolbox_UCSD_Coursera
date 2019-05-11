# Uses Python3
'''The last digit of sum of Fib(0) to Fib(n) numbers.
   We need to only sum the last digits of Fib numbers.
   But, if n is too large, this takes time. We can make
   use of Pisano period of 10: 
   Fib(n) mod m = Fib(n mod p) mod m
   because Fib(n) mod m is a periodic sequence with period p.
   That is, if g(n) = Fib(n) mod m, g(k + p) = g(k)
   The periodic sequence is called Pisano period.
   
   To compute the last digit of sums, merely compute Pisano period 
   when m = 10 (Ans. p = 60) and compute only first p Fibonaccy numbers.'''

def pisano_period(m):
    '''Compute Pisano period for m & also return the Pisano period'''
    fib_series = [0,1]
    i = 2
    while True:
        new = fib_series[i-1] + fib_series[i-2]
        fib_series.append(new)
        i += 1
        if new % m == 0:
            new = fib_series[i-1] + fib_series[i-2]
            fib_series.append(new)
            i += 1
            if new % m == 1:
                break
    return i-2, fib_series[:-2]

def fibonacci_last_digit_of_sum(n):
    # Compute Pisano period of Fib(n) modulo m as p
    ## Not required to compute p for this problem. Pisano period of 10 = 60
    p,fib_series = pisano_period(10)
    fib_series = list(map(lambda x: x % 10, fib_series))
    
    k = n // p
    r = n % p

    return (sum(fib_series) * k + sum(fib_series[:r+1])) % 10

def main():
    n = int(input())
    c = fibonacci_last_digit_of_sum(n)
    print(c)

if __name__ == "__main__":
    main()
