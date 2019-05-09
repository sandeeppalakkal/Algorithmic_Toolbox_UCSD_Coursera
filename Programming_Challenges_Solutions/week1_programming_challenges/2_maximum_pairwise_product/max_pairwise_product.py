# Uses python3
def max_product_optim1(int_list):
    n = len(int_list)
    max1 = max(int_list[0:2])
    max2 = min(int_list[0:2])
    for i in range(2,n):
        if int_list[i] < max2:
            continue
        elif int_list[i] > max1:
            max2 = max1
            max1 = int_list[i]
        elif int_list[i] > max2:
            max2 = int_list[i]
    return max1 * max2

def max_product(int_list):
    n = len(int_list)
    max_prod = int_list[0] * int_list[1]
    for i in range(n):
        for j in range(i+1,n):
            max_prod = max(int_list[i] * int_list[j],max_prod)
    return max_prod

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    assert n==len(numbers), "Array length mismatch"
    #max_prod = max_product(numbers)
    max_prod = max_product_optim1(numbers)
    print(max_prod)

if __name__ == '__main__':
    main()
