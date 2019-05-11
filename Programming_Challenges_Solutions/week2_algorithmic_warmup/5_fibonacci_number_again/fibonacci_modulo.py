# Uses Python3
'''Fib(n) mod m = Fib(n mod p) mod m
   because Fib(n) mod m is a periodic sequence with period p.
   That is, if g(n) = Fib(n) mod m, g(k + p) = g(k)
   The periodic sequence is called Pisano period.'''

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

def fibonacci_modulo(n,m):
    # Given m >= 2
    assert m >= 2
    # Compute Pisano period of Fib(n) modulo m as p
    p,fib_series = pisano_period(m)

    # Return Fib(n modulo p)
    #print(p,m)
    return fib_series[n % p] % m

def main():
    n,m = map(int, input().split())
    c = fibonacci_modulo(n,m)
    print(c)

if __name__ == "__main__":
    main()
