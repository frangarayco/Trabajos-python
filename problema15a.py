import sympy as sp
from tabulate import tabulate 
from array import array

dato=array('f',[0, 0])
mat = []
for i in range(25):
    mat.append([0]*2)
fila = 0
def cargarMat(mat,fila,dato):
    mat[fila][0] = dato[0]
    mat[fila][1] = dato[1]
    
x = sp.Symbol('x')

for n in range (1,26):
    funcion = x ** n / (x+10)
    integral = sp.integrate(funcion,(x,1,0))
    resul_i = integral.evalf()
    dato[0] = n
    dato[1] = resul_i
    cargarMat(mat,fila,dato)
    fila = fila +1


headers = ["   n      ", "         In       "]
tabla = tabulate(mat, headers=headers, tablefmt="grid", colalign=("center", "center"))
print(tabla)