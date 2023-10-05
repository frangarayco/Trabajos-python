from math import * 
from tabulate import *
from array import array


valorA=[]
valorB=[]
valorM=[]
iter=[]
mat=[]

def agregarMat(i,a,b,m,mat):
    fila=[i,a,b,m]
    mat.append(fila)
    return 


def biseccion(f, a, b, tol):
    m1=a
    m=b
    i=0
    if f(a)*f(b) > 0:
        print("Error la funcion debe tener diferente signo")
    while(abs(m1-m)>tol):
        m1=m
        m=(a+b)/2
        agregarMat(i,a,b,m,mat)
        if f(a)*f(m) < 0 : # cambia de signo en [a,m]
            b = m
        if f(b)*f(m) < 0 : # cambia de signo en [b,m]
            a=m

        i+=1
 
    headers = ["   iteraciones      ", "         Valor a:         ", "             valor b:         ", "        valor m          "]
    tabla = tabulate(mat, headers=headers, tablefmt="grid")
    print(tabla)
    print("x", i,"=",m,"es buena aproximacion")

  


    
#f = lambda x: x**3 + 4*x**2 -10
#biseccion(f,1,2,1e-6,100)

f = lambda x: x*cos(x-1)-sin(x)
biseccion(f,4.0,6.0,1e-8)


