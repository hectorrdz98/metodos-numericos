import math

a = 0.001
b = 1
n = 6
h = 6

def f(x):
    return (math.sin(x) / x)

# x = [ a + (i*h) for i in range(n+1) ]
x = [0, 6, 12, 18, 24, 30, 36, 42, 54, 60, 66, 72, 78, 84]
# print('x = {}'.format(x))

# fx = [ f(xi) for xi in x ]
fx = [124, 134, 148, 156, 147, 133, 121, 109, 85, 78, 89, 104, 116, 123]
# print('fx = {}'.format(fx))

T = (h/2) * (fx[0] + ( 2 * (sum([ fx[xi] for xi in range(1, len(fx)-1) ])) ) + fx[len(fx)-1])
print('T = {}'.format(T))