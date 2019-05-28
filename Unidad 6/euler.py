import math
import numpy as np
from prettytable import PrettyTable

x0 = 1
y0 = 1
xF = 1.5
n = 5

decimals = 4

h = (xF-x0) / n
print('\nh: {}\n'.format(h))

def dydx(x, y):
    return 2*x*y

xi = [ x0 + (i*h) for i in range(n+1) ]
yi = [ 0 for i in range(n+2) ]

yi[0] = y0

cont = 0

t = PrettyTable(['i', 'xi', 'yi', 'f(xi,yi)', 'yi+1'])
# dydx = f(x,y), yi+1 = yi+hf(xi,yi)

for x in xi:
    fxiyi = np.round(dydx(x, yi[cont]), decimals=decimals)
    yi[cont+1] = np.round(yi[cont] + (h * fxiyi), decimals=decimals)
    t.add_row([cont, x, yi[cont], fxiyi, yi[cont+1]])
    cont += 1

print(t)
        