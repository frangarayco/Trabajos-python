from math import *

def puntofijo (f,p0,error,n):
    i=1
    while (i <= n):
        p = f(p0)
        print (" Iter = " , " %03d" % i, " ; p = " , " %.14f" % p)
        if (abs(p-p0) < error):
            return p
        p0 = p
        i += 1
    print ("Iteraciones terminadas: error")
    return  


f = lambda x: (x**2-1) /3
puntofijo(f,0.9, 1e-10,100)


