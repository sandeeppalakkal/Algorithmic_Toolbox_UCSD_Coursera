# Uses Python3
'''A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
   of items assuming that any fraction of a loot item can be put into his bag.'''

'''Problem Description
   Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
   Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
   The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
   value and the weight of 𝑖-th item, respectively.
   Constraints. 1 ≤ 𝑛 ≤ 10e3, 0 ≤ 𝑊 ≤ 2 · 10e6; 0 ≤ 𝑣𝑖 ≤ 2 · 10e6, 0 < 𝑤𝑖 ≤ 2 · 10e6 for all 1 ≤ 𝑖 ≤ 𝑛. 
   All the numbers are integers.
   Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
   value of the difference between the answer of your program and the optimal value should be at most
   10−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise
   your answer, while being computed correctly, can turn out to be wrong because of rounding issues).'''

def max_items_frac_value(v,w,max_w):
    cur_w = 0
    cur_v = 0
    n = len(v)
    v_per_w = [x / y for (x,y) in zip(v,w)]
    #print(v,w,v_per_w)
    for i in range(n):
        max_v_id = v_per_w.index(max(v_per_w))
        cur_item_v = v.pop(max_v_id)
        cur_item_w = w.pop(max_v_id)
        cur_item_vpw = v_per_w.pop(max_v_id)
        if cur_w + cur_item_w <= max_w:
            cur_v += cur_item_v
            cur_w += cur_item_w
        else:
            frac = (max_w - cur_w) /cur_item_w
            cur_v += frac * cur_item_v
            cur_w += frac * cur_item_w
            break
    return cur_v
    
def main():
    n,max_w = map(int,input().split())
    v = []
    w = []
    for i in range(n):
        vi,wi = map(int,input().split())
        v.append(vi)
        w.append(wi)
    max_v = max_items_frac_value(v,w,max_w) 
    print('%.3f'%max_v)

if __name__ == '__main__':
    main()
