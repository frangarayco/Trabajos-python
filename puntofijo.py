from math import *
from tabulate import *


mat = []


def cargarMat(p,p0,i,f):
    fila =[i,p0,p,f(p)]
    mat.append(fila)
    return

def puntofijo (f,p0,tol,iterMax):
    i = 0
    while i < iterMax : 
        p = f(p0)
        if (abs(p-p0) < tol):
            break
        cargarMat(p,p0,i,f)
        p0 = p
        i += 1

        
    headers = ["   iteraciones      ", "         Valor p0:         ","       Valor de p          ","             Valor de f(p):         "]
    tabla = tabulate(mat, headers=headers, tablefmt="grid")
    print(tabla)


    return p
      
    
      


f = lambda x: (x**2-1) /3
puntofijo(f,0.9, 1e-10,10)


