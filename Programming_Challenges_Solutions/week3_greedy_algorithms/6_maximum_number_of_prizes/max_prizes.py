# Uses Python3
'''Maximum Number of Prizes
Problem Introduction
You are organizing a funny competition for children. As a prize fund you have 𝑛
candies. You would like to use these candies for top 𝑘 places in a competition
with a natural restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest
value of 𝑘 for which it is possible.
Problem Description
Task. The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
Input Format. The input consists of a single integer 𝑛.
Constraints. 1 ≤ 𝑛 ≤ 1e9.
Output Format. In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum
of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers
that sum up to 𝑛 (if there are many such representations, output any of them).'''

#import time

def max_prizes(n):
    j = 0
    a = []
    while n > 0:
        j += 1
        m = n - j
        if m > j or m == 0:
            a.append(j)
            n = m
        else:
            continue
    return a

def main():
    n = int(input())
    #t1 = time.time()
    prizes = max_prizes(n)
    #t2 = time.time()
    k = len(prizes)
    print(k)
    for p in prizes:
        print(p,end=' ')
    print()
    #print("time taken = %f" % (t2-t1))

if __name__ == '__main__':
    main()
