from math import *
from tabulate import tabulate 
from array import array 


valorA = []
valorB = []
valorP = []
valorFP = []
valorError = []

def cargar (a,b,p,f,error):
    valorA.append(a)
    valorB.append(b)
    valorP.append(p)
    valorFP.append(f(p))
    valorError.append(error)
    return
 

def regula(f, a, b,error):
    i = 0
    if (f(a) * f(b) > 0 ):
        print("Los valores estan mal")
    
    p = a -((f(a)*(b-a))/(f(b)-f(a)))

    while(abs(f(p)) > error):
        p = a -((f(a)*(b-a))/(f(b)-f(a)))
        print(" Iter = " , " %03d" % i, " ; p = " , " %.14f" % p)
        if (abs(f(p)) < error):
            break
        elif (f(a)*f(b) > 0):
            a = p
        else:
            b = p
        
        i += 1
    return (p)
f = lambda x: x*cos(x-1)-sin(x)
regula(f,4,6,1e-8)






#f = lambda x: x**3+4*x**2-10
#regula(f,1,2,1e-8,100)

cargar(a,b,p,f,error)
        
    cargar(a,b,p,f,error)
    
    mat={
        "Iteracion": i,
        "Valor en f(p)": valorFP,
        "Error": valorError
    }

    headers = ["   Iteraciones      ", "         f(p)        ", "             Error             "]
    tabla = tabulate(mat, headers=headers, tablefmt="grid", colalign=("center", "center", "center"))
    print(tabla)