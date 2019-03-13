import math

x0 = 1.9
n = 3
tol = 0.0001

def f(x):
    return -4 + (4*x) - (0.5 * x * x)

def fprime(x):
    return 4 - x

flag = False

for i in range(n):
    x1 = x0 - (f(x0)/fprime(x0))
    print('\nVoy en x0={} y f(x)={}, f´(x0)={}'.format(x0,f(x0),fprime(x0)))
    print('x1 vale {}'.format(x1))
    if math.fabs(x0-x1) <= tol:
        print('\nLlegué a la tol con {} ite, x1={}'.format(i+1, x1))
        flag = True
        break
    x0 = x1

if not flag:
    print('\nHice las {} iter y no llegué a la tol, x1={}'.format(n, x1))
    