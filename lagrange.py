from math import * 

def lagrange (datos): 
    def L(k, x):
        out = 1
        for i, p in enumerate(datos):
            if (i != k):
                out *= (x-p[0])/(datos[k][0]-p[0])
        return out
    
    def P(x): 
        lag= 0
        for k, p in enumerate(datos):
            lag += p[1]*L(k,x)
        return lag
    
    return P

#datos = [(2.0, 1.0/2.0), (11.0/4.0, 4.0/11.0), (4.0, 1.0/4.0)]
#Pf = lagrange(datos)
#print (Pf(3))


datos =[(1.0, 0.1411), (1.3, -0.6878), (1.6, -0.9962), (1.9, -0.5507), (2.2, 0.3115)]
pf = lagrange(datos)
print(pf(1.5))