# Uses Python3

'''Closest Points
Problem Introduction
In this problem, your goal is to find the closest pair of points among the given 𝑛
points. This is a basic primitive in computational geometry having applications in,
    for example, graphics, computer vision, traffic-control systems.
    Problem Description
    Task. Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. Recall
    that the distance between points (𝑥1, 𝑦1) and (𝑥2, 𝑦2) is equal to
    √︀
    (𝑥1 − 𝑥2)2 + (𝑦1 − 𝑦2)2.
    Input Format. The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point
    (𝑥𝑖, 𝑦𝑖).
    Constraints. 2 ≤ 𝑛 ≤ 1e5; −1e9 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 1e9 are integers.
    Output Format. Output the minimum distance. The absolute value of the difference between the answer
    of your program and the optimal value should be at most 10−3. To ensure this, output your answer
    with at least four digits after the decimal point (otherwise your answer, while being computed correctly,
            can turn out to be wrong because of rounding issues).'''

import numpy as np

def min_dist_brute(a):
    assert len(a) >= 2
    min_d = np.linalg.norm(a[0]-a[1],2)
    for i,p in enumerate(a[:-1]):
        for q in a[i+1:]:
            d = np.linalg.norm(p-q,2)
            min_d = min(d,min_d)
    return min_d

def min_dist_stip(strip,d):
    if strip.size == 0:
        return d
    min_d = d
    # sort by y coords
    strip = strip[strip[:,1].argsort(kind='heapsort')]
    for i,p in enumerate(strip[:-1]):
        for q in strip[i+1:]:
            if abs(p[1] - q[1]) >= d:
                break
            d = np.linalg.norm(p-q,2)
            min_d = min(min_d,d)
    return min_d

def make_strip(a,a_mid,d):
    strip = []
    for p in a:
        if abs(p[0] - a_mid[0]) < d:
            strip.append(p)
    return np.array(strip)

def min_dist_util(a,m,n):
    if (n - m) <= 3:
        return min_dist_brute(a[m:n])

    mid = (m + n) // 2
    
    # Recurse on left & right arrays
    dl = min_dist_util(a,m,mid)
    dr = min_dist_util(a,mid,n)
    d = min(dl,dr)

    # array with horizontal points closer than d in the middle
    strip = make_strip(a[m:n],a[mid],d)

    # find min distance in strip, smaller than d
    d_strip = min_dist_stip(strip,d)

    return d_strip


def min_dist(a):
    # Sort points according to x coords
    a = a[a[:,0].argsort(kind='heapsort')]

    # Recursively find smallest distance
    return min_dist_util(a,0,len(a))

def main():
    n = int(input())
    a = np.zeros((n,2))
    for i in range(n):
        a[i] = list(map(int,input().split()[:2]))
    d = min_dist(a)
    #d = min_dist_brute(a)
    print('%.4f' % d)

if __name__ == '__main__':
    main()
