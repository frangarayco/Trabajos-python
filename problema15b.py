import sympy as sp
from tabulate import tabulate 
from array import array

dato=array('f',[0, 0])
mat = []
for i in range(24):
    mat.append([0]*2)
fila = 0
def cargarMat(mat,fila,dato):
    mat[fila][0] = dato[0]
    mat[fila][1] = dato[1]
    
def funcion(r,n):
    return (1/10) * (1/n-r)

x= sp.Symbol('x')

valores = [i for i in range(1,25)]

resuAnt = sp.integrate((x ** 0) / (x + 10), (x, 1, 0)).evalf()

for n in valores:
    funActual = (x ** n) / (x + 10)
    integral = sp.integrate(funActual,(x,1,0))
    resu_i = integral.evalf()

    resuActual = funcion(resuAnt, n)

    dato[0] = n
    dato[1] = resuActual
    cargarMat(mat,fila,dato)
    fila = fila + 1
    resuAnt = resuActual


headers = ["   n      ", "         In       "]
tabla = tabulate(mat, headers=headers, tablefmt="grid", colalign=("center", "center"))
print(tabla)
resul25 = resuAnt
print (f"I25 ≈ I24: {resul25}")
      