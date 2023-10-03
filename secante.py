from math import *

def secante(f, p0, p1, error, n): 
    i = 2
    while (i <=n):
        p = p1 - (f(p1)*(p1-p0))/(f(p1)-f(p0))
        print(" Iter = " , " %03d" % i, " ; p = " , " %.14f" % p)
        if(abs(p-p1) < error):
            return p
        p0 = p1
        p1 = p
        i += 1
    print("Iteraciones terminadas, error")
    return 

f = lambda x: (sin(2/x))
secante(f, 1.1, 0.8, 1e-8, 100)