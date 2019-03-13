import math

p0 = 3.8
n = 3
tol = 0.0001

def g(p):
    return -4 + (4*p) - (0.5 * p * p)

flag = False

for i in range(n):
    p = g(p0)
    print('\nVamos en {}, con g(p0)={} y p0={}'.format(i+1,g(p0),p0))
    print('El abs={}'.format(math.fabs(p-p0)))
    if math.fabs(p-p0) <= tol:
        print('\nEl valor de p0={} ya se encuentra dentro de la tol de {} con {} ite'.format(p0,tol,i+1))
        flag = True
        break
    p0 = p

if not flag:
    print('\nSe realizaron las {} iteraciones, pero no se llegó a la tol de {}'.format(n,tol))
    print('Se llegó a p0={}'.format(p0))