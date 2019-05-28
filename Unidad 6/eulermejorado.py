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

xi = [ x0 + (i*h) for i in range(n+2) ]
yi = [ 0 for i in range(n+2) ]

yi[0] = y0

cont = 0

t = PrettyTable(['i', 'xi', 'yi', 'f(xi,yi)', 'yi+1*', 'f(xi+1,yi+1*)', 'yi+1'])
# dydx = f(x,y), yi+1* = yi+hf(xi,yi), yi+1 = (h/2) * (f(xi,yi) + f(xi+1,yi+1*))

for x in xi:
    if cont < len(xi) - 1:
        fxiyi = np.round(dydx(x, yi[cont]), decimals=decimals)
        yiEstrella = np.round(yi[cont] + (h * fxiyi), decimals=decimals)
        fxiyiEstrella = np.round(dydx(xi[cont+1], yiEstrella), decimals=decimals)
        yi[cont+1] = np.round(yi[cont] + ((h/2) * (fxiyi + fxiyiEstrella)), decimals=decimals)
        t.add_row([cont, x, yi[cont], fxiyi, yiEstrella, fxiyiEstrella, yi[cont+1]])
        cont += 1

print(t)