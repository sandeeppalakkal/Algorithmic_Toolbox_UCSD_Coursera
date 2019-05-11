# Uses Python3
'''LCM computation'''
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

def lcm_through_gcd(a,b):
    '''LCM = abs(a * b) / GCD(a,b)'''
    g = gcd_reminder(a,b)
    return a * b // g

def  lcm_addition(a,b):
    '''LCM should be smallest multiple  of b divisible by a, when b > a'''
    a,c = sort(a,b)
    while(c % a != 0):
        c += b
    return c

def main():
    a,b = map(int, input().split())
    start_time = time.time()
    c = lcm_through_gcd(a,b)
    end_time = time.time()
    print(c)
    #print("time elapsed: %f" % (end_time - start_time))

if __name__ == '__main__':
    main()
