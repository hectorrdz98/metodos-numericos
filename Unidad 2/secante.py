import math

x0 = math.pi / 4
x1 = 0
n = 20
tol = 0.001

def f(x):
    return math.cos(x) - x

flag = False

for i in range(n):
    x2 = x1 - (f(x1)*(x1-x0)) / (f(x1)-f(x0))
    #print('\nVoy en x0={} y x1={}\nf(x0)={} y f(x1)={}'.format(x0,x1,f(x0),f(x1)))
    #print('x2 vale {}'.format(x2))
    if math.fabs(x2-x1) <= tol:
        print('\nLlegué a la tol con {} ite, x2={}'.format(i+1, x2))
        flag = True
        break
    x0 = x1
    x1 = x2

if not flag:
    print('\nHice las {} iter y no llegué a la tol, x1={}'.format(n, x1))
    