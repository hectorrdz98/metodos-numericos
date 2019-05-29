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

def f(x, y):
    return 2*x*y

xi = [ x0 + (i*h) for i in range(n+2) ]
yi = [ 0 for i in range(n+2) ]

yi[0] = y0

cont = 0

t = PrettyTable(['i', 'xi', 'yi', 'k1', 'k2', 'k3', 'k4', 'yi+1'])

for x in xi:
    if cont < len(xi) - 1:

        k1 = np.round(h * f(x,           yi[cont]),             decimals=decimals)
        k2 = np.round(h * f(x + (h/2),   yi[cont] + (k1/2)),    decimals=decimals)
        k3 = np.round(h * f(x + (h/2),   yi[cont] + (k2/2)),    decimals=decimals)
        k4 = np.round(h * f(x + h,       yi[cont] + k3),        decimals=decimals)

        yi[cont+1] = np.round(yi[cont] + ((1/6) * (k1 + 2*k2 + 2*k3 + k4 )), decimals=decimals)
        
        t.add_row([cont, x, yi[cont], k1, k2, k3, k4, yi[cont+1]])
        cont += 1

print(t)