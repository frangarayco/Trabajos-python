

def trapecio (f,a,b,n):
    h = (b-a)/n 

    suma = 0.5 * (f(a)+f(b))
    for i in range(1, n): 
        suma += f(a+i*h)
    resu = h*suma
    return resu 
        
f = lambda x: x**3-6*x**2+11*x-6

print(trapecio(f,1.3,1.8,10))