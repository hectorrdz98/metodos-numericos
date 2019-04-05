import math

"""a = float(input('Ingresa a: '))
b = float(input('Ingresa b: '))
n = int(input('Ingresa n: '))
tol = float(input('Ingresa tol: '))"""
a = 4
b = 5
n = 1000
tol = 0.01

def g(x):
    return (x*x*x + 4*x*x - 10)

def f(x):
    #return ((1/math.sqrt(2*math.pi))*math.exp(-0.5*x*x)) + (0.1*math.sin(math.pi*x))
    return 20406.25 - (804.25*x) - (20106.25 * math.exp(-0.04*x))

p = 0
flag = False

print()

for i in range(n):
    p = a + (b-a) / 2
    print('Vamos en i={}.\na: f({}) = {}.\nb: f({}) = {}.\np: f({}) = {}\n'.format(i+1,a,f(a),b,f(b),p,f(p)))
    if f(p) == 0:
        print('{} es una raiz, con ite={}'.format(p, i+1))
        flag = True
        break
    if b - a <= tol:
        print('(b): {} - (a): {} ya está dentro de la tolerancia de {} con ite={}'.format(b, a, tol, i+1))
        print('p: {}'.format(p))
        flag = True
        break
    if i < n-1:
        if f(p)*f(a) < 0:
            b = p
        else:
            a = p
if not flag:
    print('Realizé las {} iteraciones, no llegué a la tol de {}...'.format(n, tol))
    print('(a): {} (b): {} y (p): {}'.format(a,b,p))