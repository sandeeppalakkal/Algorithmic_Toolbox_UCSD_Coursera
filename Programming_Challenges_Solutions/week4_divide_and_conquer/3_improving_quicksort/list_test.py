def list_update_(b):
    print('got ',b)
    b[0] = 100
    return
def list_update(a):
    n = len(a)
    list_update_(a[:n//2])
    list_update_(a[n//2:])
    return 

a = [1,2,3,4]
print(a)
list_update(a)
print(a)
