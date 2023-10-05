from math import *
from tabulate import *


mat=[]
def agregarMat(i,p1,f,mat):
    
    fila=[i,p1,f(p1)]
    mat.append(fila)
    return




def newton(f,fprima,p0,tol):
    p1=p0
    i= 1
    while(f(p0) > tol or f(p0) < (-tol)):
        p1=p0-f(p0)/fprima(p0)
        if(abs(p1-p0) < tol):
            #print("x",i+1,"=",p1,end="")
            agregarMat(i,p1,f,mat)
            return
        p0=p1
        #print("x",i+1,"=",p1)
        agregarMat(i,p1,f,mat)
        i += 1
        

    headers = ["   iteraciones      ", "         Valor de la raiz:         ", "             Raiz evaluada:         "]
    tabla = tabulate(mat, headers=headers, tablefmt="grid")
    print(tabla)
    return(p1)


f = lambda x: cos(x)-x
fprima = lambda x: -sin(x)-1
newton(f,fprima, pi/4, 1e-10)   


#f = lambda x: x**2+exp(-2*x)-2*x*exp(-x)
#fprima = lambda x: 2*x-2*exp(-2*x)-2*exp(-x)+2*x*exp(-x)
#newton(f,fprima,4,1e-8)
