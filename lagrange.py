import numpy as np 
from sympy import *


def polL(xi,fi): 
    x = Symbol("x")
    n = len(xi)
    pol=0
    for i in range(n):
        numerador=1
        denominador=1
        for j in range(n):
            if j != i:
                numerador *=(x-xi[j])
                denominador *= (xi[i]-xi[j])
        termino=numerador/denominador 
        pol+=termino*fi[i]  
    return pol  


def polL_eval(xi,fi,a): 
    resu=0
    for i in range(len(xi)):
        numerador=1
        denominador=1
        for j in range(len(xi)):
            if j != i:
                numerador *=(a-xi[j]) #aca reemplazo a, que es el valor donde quiero evaluar el polinomio de lagrange
                denominador *= (xi[i]-xi[j])
        termino=numerador/denominador 
        resu+=termino*fi[i]  
    return resu  
        


xi= np.array([1.0,1.3,1.6,1.9,2.2])
fi= np.array([0.1411,-0.6878,-0.9962,-0.5507,0.3115])
a = 1.5
print(polL(xi,fi))
print("El valor de polinomio evaluado en {a} es:", polL_eval(xi,fi,a))
