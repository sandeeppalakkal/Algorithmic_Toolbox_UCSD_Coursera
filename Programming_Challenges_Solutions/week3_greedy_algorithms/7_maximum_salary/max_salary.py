# Use Python3

'''Problem Description
Task. Compose the largest number out of a set of integers.
Input Format. The first line of the input contains an integer 𝑛. The second line contains integers
𝑎1, 𝑎2, . . . , 𝑎𝑛.
Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 1e3 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format. Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.'''

def check_order(a,b,mode = 'ASC'):
    '''Check order of a & b: if ascending (b>a) or descending (b<a)'''
    if mode == 'ASC':
        return not b == min(a,b)
    elif mode == 'DESC':
        return not b == max(a,b)

def check_num_concat_order(a,b,mode='DESC'):
    '''For max salary, check order by concatenating in different order'''
    c = int(str(a) + str(b))
    d = int(str(b) + str(a))
    return check_order(c,d,'DESC')
    
def arrange_around_pivot(a,p,i,j,order):
    k = i
    while i < j and k <= j:
        #if check_order(a[k],p,order):
        if check_num_concat_order(a[k],p,order):
            t = a[i]
            a[i] = a[k]
            a[k] = t
            i += 1
            k += 1
        #elif check_order(p,a[k],order):
        elif check_num_concat_order(p,a[k],order):
            t = a[j]
            a[j] = a[k]
            j -= 1
            a[k] = t
        else:
            k += 1
    return i

def quick_sort(a,i,j,order='ASC'):
    if i >= j:
        return
    p = a[i]
    pi = arrange_around_pivot(a,p,i,j,order)
    quick_sort(a,i,pi-1,order)
    quick_sort(a,pi+1,j,order)
    return

def sort(a,order='ASC'):
    quick_sort(a,0,len(a)-1,order)

def max_salary(a):
    n = len(a)
    sort(a,'DESC')
    b = ''.join([str(x) for x in a])
    return b

def main():
    n = int(input())
    a = [int(x) for x in input().split()[:n]]
    s = max_salary(a)
    print(s)

if __name__ == '__main__':
    main()
