# Uses Python3
'''Binary Search
In this problem, you will implement the binary search algorithm that allows searching
very efficiently (even huge) lists, provided that the list is sorted.'''

'''Problem Description:
Task. The goal in this code problem is to implement the binary search algorithm.
Input Format. The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1
of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘
positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
Constraints. 1 ≤ 𝑛, 𝑘 ≤ 104; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 109 for all 0 ≤ 𝑗 < 𝑘;
Output Format. For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
is no such index.'''

def binary_search(target,array,l,r):
    n = r - l + 1
    if n == 1:
        if array[l] == target:
            return l
        else:
            return -1
    mid = (l + r) // 2
    if target <= array[mid]:
        index = binary_search(target,array,l,mid)
    else:
        index = binary_search(target,array,mid+1,r)
    if index == -1:
        return index
    else:
        return index

def search_and_index(a,b):
    index = [0] * len(b)
    for i,t in enumerate(b):
        index[i] = binary_search(t,a,0,len(a)-1)
    return index

def main():
    a = list(map(int,input().split()))
    n = a.pop(0)
    assert n == len(a)
    b = list(map(int,input().split()))
    k = b.pop(0)
    assert k == len(b)

    index = search_and_index(a,b)
    for i in index:
        print(i, end=" ")
    print()

if __name__ == '__main__':
    main()
