import math

def trapecio(f, a, b, n):
    h = (b - a) / n
    int = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        int += f(a + i * h)
    return h * int

def romberg(f, a, b, n):
    mat_rom = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        mat_rom[i][0] = trapecio(f, a, b, 2**i)
    
    for j in range(1, n+1):
        for i in range(j, n+1):
            mat_rom[i][j] = (4**j * mat_rom[i][j-1] - mat_rom[i-1][j-1]) / (4**j - 1)
    
    return mat_rom[n][n]

f = lambda x: x*math.log(x)

resu = romberg(f, 1, 2, 10)
print("El resultado de la integral es: ", resu)
