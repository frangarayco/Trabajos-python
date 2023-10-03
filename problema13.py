import math
from array import array
from tabulate import tabulate

def f(x):
    return math.exp(x)

def cargarMat(mat,fila,dato):
    mat[fila][0] = dato[0]
    mat[fila][1] = dato[1]
    mat[fila][2] = dato[2]
    
dato=array('f',[0, 0, 0])
mat = []
for i in range(31):
    mat.append([0]*3)

fila = 0
x=0
exact_result = f(x)
print("valor exacto de f(x) = ", exact_result)

for i in range(1, 31):
    h = 2 ** -i
    aprox_result = (f(x+h)-f(x))/h
    error_absoluto = abs(aprox_result - exact_result)
    dato[0] = i
    dato[1]= aprox_result
    dato[2] = error_absoluto
    cargarMat(mat,fila,dato)
    fila = fila + 1

    
headers = ["   h      ", "         Resu Aprox        ", "             Error Abs            "]
tabla =tabulate(mat, headers=headers, tablefmt="grid", colalign=("center", "center", "center"))
print(tabla)