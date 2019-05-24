def list_update_(b,m,n):
    print('got ',b)
    b[m] = 100
    return
def list_update(a):
    n = len(a)
    list_update_(a,0,n//2)
    list_update_(a,n//2,n)
    return 

a = [1,2,3,4]
print(a)
list_update(a)
print(a)
