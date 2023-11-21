


def simpson(f,a,b,n): 
    if (n % 2 != 0): 
        raise ValueError("El numero de subinvertavlos no es par")
    h = (b-a)/n
    valorX = [a + i * h for i in range(n+1)]
    integral =  f(a) + f(b)
    for i in range(1,n):
        if i % 2 == 0: 
            integral += 2 * f(valorX[i])
        else: 
            integral += 4 * f(valorX[i])
    integral *= h / 3
    print (integral)
    return integral 


f = lambda x: x**3+ x**2 + x + 1
simpson(f,1,2,10)
