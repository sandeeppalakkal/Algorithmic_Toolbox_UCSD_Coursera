# Uses Python3
'''GCD can be computed recursively'''

import time

def sort(a,b):
    if a < b:
        return a,b
    else:
        return b,a

def gcd_reminder(a,b):
    '''Since gcd divides a & b, it divides reminder of b/a, assuming a < b'''
    a,b = sort(a,b)
    r = b % a
    if r == 0: return a
    else: return gcd_reminder(a,r)

def gcd_subtraction(a,b):
    '''Since gcd divides a & b, it divides (b-a), if a < b'''
    a,b = sort(a,b)
    if (b % a == 0):
        return a
    else:
        return gcd_subtraction(a,b-a)

def main():
    a,b = map(int, input().split())
    start_time = time.time()
    #c = gcd_subtraction(a,b)
    c = gcd_reminder(a,b)
    end_time = time.time()
    print(c)
    #print("time elapsed: %f" % (end_time - start_time))

if __name__ == '__main__':
    main()
