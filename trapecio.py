

def trapecio (f,a,b):
    return ((b-a)*(f(a)+f(b)))/2


f = lambda x: x**3-6*x**2+11*x-6

print(trapecio(f,1.3,1.8))