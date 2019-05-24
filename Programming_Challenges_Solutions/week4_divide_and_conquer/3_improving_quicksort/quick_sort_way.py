# Uses Python3

'''Improving Quick Sort
Problem Introduction
The goal in this problem is to redesign a given implementation of the randomized
quick sort algorithm so that it works fast even on sequences containing many equal elements.'''

'''Problem Description
Task. To force the given implementation of the quick sort algorithm to efficiently process sequences with
few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.
Input Format. The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints. 1 ≤ 𝑛 ≤ 10e5; 1 ≤ 𝑎𝑖 ≤ 10e9 for all 0 ≤ 𝑖 < 𝑛.
Output Format. Output this sequence sorted in non-decreasing order.'''

def partition3(a,l,r):
    p = a[l]
    lt = l
    gt = r+1
    i = l+1
    while i < gt:
        if a[i] < p:
            lt += 1
            a[lt],a[i] = a[i],a[lt]
            i += 1
        elif a[i] > p:
            gt -= 1
            a[gt],a[i] = a[i],a[gt]
        else:
            i += 1
    a[lt],a[l] = a[l],a[lt]
    return lt,gt-1

def partition2(a,l,r):
    # Pivot
    p = a[r]
    i = l
    j = r
    while i < j:
        if a[i] > p:
            j -= 1
            a[i],a[j] = a[j],a[i]
        else:
            i += 1
    a[j],a[r] = a[r],a[j]
    return i

def quick_sort(a,l,r):
    if r <= l:
        return
    m,n = partition3(a,l,r)
    quick_sort(a,l,m-1)
    quick_sort(a,n+1,r)
    return

def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a[:n]]
    quick_sort(a,0,n-1)
    for i in range(n):
        print(a[i], end=" ")
    print()

if __name__ == '__main__':
    main()
