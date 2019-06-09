# Uses Python3
'''Number of Inversions
Problem Introduction
An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such
that 𝑎𝑖 > 𝑎𝑗 . The number of inversions of a sequence in some sense measures how
close the sequence is to being sorted. For example, a sorted (in non-descending
        order) sequence contains no inversions at all, while in a sequence sorted in descending
order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2
        inversions).

Problem Description
Task. The goal in this problem is to count the number of inversions of a given sequence.
Input Format. The first line contains an integer 𝑛, the next one contains a sequence of integers
𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints. 1 ≤ 𝑛 ≤ 1e5, 1 ≤ 𝑎𝑖 ≤ 1e9 for all 0 ≤ 𝑖 < 𝑛.
Output Format. Output the number of inversions in the sequence.'''

def merge(a,b):
    n1 = len(a)
    n2 = len(b)
    n = n1 + n2
    c = []
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            # Inversion: b[j] is jumping back by n1-i numbers in a
            k += n1-i
    while i < n1:
        c.append(a[i])
        i += 1
    while j < n2:
        c.append(b[j])
        j += 1
    return c,k

def merge_sort(a,i=None,j=None):
    if i == None:
        i = 0
    if j == None:
        j = len(a)
    n = j - i
    if n == 1:
        k = 0
        b = a[i:j]
    else:
        m = (i + j)//2
        a1,k1 = merge_sort(a,i,m)
        a2,k2 = merge_sort(a,m,j)
        b,k3 = merge(a1,a2)
        k = k1 + k2 + k3
    return b,k

def inversions(a):
    b,m = merge_sort(a)
    return m

def main():
    n = int(input())
    a = list(map(int,input().split()[:n]))
    k = inversions(a)
    print(k)

if __name__ == '__main__':
    main()
