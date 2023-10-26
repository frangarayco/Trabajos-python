import sympy
import numpy as np
import matplotlib.pyplot as plt

def cuadradoMinimo(datox,datoy):
    x = sympy.Symbol('x')
    sumx= 0
    sumy = 0
    sumxy = 0
    sumx2 = 0
    n = len(datox)

    for i in range (len(datox)):
        sumx  = sumx + datox[i]
        sumy = sumy + datoy[i]
        sumxy = sumxy + (datox[i]*datoy[i])
        sumx2 = sumx2 + datox[i]**2

    m = ((n*sumxy)-(sumx*sumy))/((n*sumx2)-(sumx**2))
    b = (sumy- m * sumx)/  n

    plt.plot(datox,datoy, "o", label="Puntos")
    plt.plot(datox, m*np.array(datox) + b, label= m*x+b)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Grafico cuadrado minimo")
    plt.grid()
    plt.legend (loc = 4)
    plt.show()
    return (m*x+b)


datox = [0, 2, 4, 6, 8, 10, 12, 14]
datoy = [25, 28.1, 35.2, 36.2, 41.3, 42.1, 47.9, 54.2]
cuadradoMinimo(datox,datoy)