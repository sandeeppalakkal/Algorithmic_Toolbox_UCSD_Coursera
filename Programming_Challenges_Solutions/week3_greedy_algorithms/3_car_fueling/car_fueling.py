# Uses Python3
'''You are going to travel to another city that is located 𝑑 miles away from your home city. Your can can travel
at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?'''

'''Problem Description
Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
on a full tank, and there are gas stations at distances stop1, stop2, . . . , stop𝑛 along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
Constraints. 1 ≤ 𝑑 ≤ 105. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.'''

def min_fuel_stops(d,m,gas_stns):
    gas_stns.append(d)
    n_stns = len(gas_stns)
    n_stops = 0
    dist_travelled = 0
    i = 0
    j = -1
    while i < n_stns:
        dist_to_travel = gas_stns[i] - dist_travelled
        if dist_to_travel > m:
            i -= 1
            if j == i:
                n_stops = -1
                break
            j = i
            dist_travelled = gas_stns[j]
            n_stops += 1
        else:
            i += 1
    return n_stops

def main():
    d = int(input())
    m = int(input())
    n = int(input())
    gas_stns = list(map(int,input().split()))
    min_stops = min_fuel_stops(d,m,gas_stns)
    print(min_stops)

if __name__ == '__main__':
    main()
