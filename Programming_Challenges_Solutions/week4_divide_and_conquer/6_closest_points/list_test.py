import numpy as np

def fun(a):
    print(a)

a = [1,2,3,4,5,6,7,8]
fun(a[3:6])

b = np.array(a)
fun(b[3:6])
