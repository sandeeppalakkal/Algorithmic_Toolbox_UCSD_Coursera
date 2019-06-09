# Uses Python3

'''Problem Description
Task. Given a set of 𝑛 segments {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} with integer coordinates on a line, find
the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a
set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖, 𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such

that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.
Input Format. The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines
contains two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th
segment.

Constraints. 1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.
Output Format. Output the minimum number 𝑚 of points on the first line and the integer coordinates
of 𝑚 points (separated by spaces) on the second line. You can output the points in any order. If there
are many such sets of points, you can output any set. (It is not difficult to see that there always exist
a set of points of the minimum size such that all the coordinates of the points are integers.)'''

import numpy as np

#def consists(t,p):


def intersect(a):
    # Sort by second number
    a = a[a[:,1].argsort()]
    # Select the second number as intersect
    sect = [a[0,1]]
    for p in a:
        #if not consists(sect[-1],p):
        if p[0] > sect[-1]:
            sect.append(p[1])
    return sect

def main():
    n = int(input())
    a = np.zeros((n,2),dtype=int)
    for i in range(n):
        a[i] = [int(x) for x in input().split()[:2]]
    sect = intersect(a)
    m = len(sect)
    print(m)
    for s in sect:
        print(s,end=' ')
    print()

if __name__ == '__main__':
    main()
