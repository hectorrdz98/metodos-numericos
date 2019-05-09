import math

a = 500
b = 1800
n = 1
h = (b-a) / n

def f(x):
    return math.sin(x)

# x = [ a + (i*h) for i in range(n+1) ]
x = [500, 1800]
print('x = {}'.format(x))

# fx = [ f(xi) for xi in x ]
fx = [ 9, 23 ]
print('fx = {}'.format(fx))

T = (h/2) * (fx[0] + ( 2 * (sum([ fx[xi] for xi in range(1, len(fx)-1) ])) ) + fx[len(fx)-1])
print('T = {}'.format(T))