import math

a = 2
b = 7
n = 22822
h = (b-a) / n

def f(x):
    return (1/x)

x = [ a + (i*h) for i in range(n+1) ]
# x = [500, 1150, 1800]
# print('x = {}'.format(x))

fx = [ f(xi) for xi in x ]
# fx = [ 9, 16.1, 23 ]
# print('fx = {}'.format(fx))

S = (h/3) * (fx[0] + ( 2 * (sum([ fx[xi] for xi in range(2, len(fx)-2, 2) ])) ) + ( 4 * (sum([ fx[xi] for xi in range(1, len(fx)-1, 2) ])) ) + fx[len(fx)-1])
print('S = {}'.format(S))