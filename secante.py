from math import *
from tabulate import *



mat=[]

def cargarMat(p0,p1,p,i,f):
    fila = [i,p0,p1,p,f(p)]
    mat.append(fila)
    return


def secante(f, p0, p1, tol):
    i=1 
    p = p1
    while (abs(f(p)) > tol):
        p = p1 - (f(p1)* (p1-p0)) / (f(p1)-f(p0))
        if (abs(f(p)) < tol):
            break
        p0 = p1
        p1 = p
        cargarMat(p0,p1,p,i,f)
        i += 1
    
    headers = ["   iteraciones      ", "         Valor p0:         ", "     Valor de P1       ","       Valor de p          ","             Valor de f(p):         "]
    tabla = tabulate(mat, headers=headers, tablefmt="grid")
    print(tabla)

f = lambda x: (sin(2/x))
secante(f, 1.1, 0.8, 1e-8)