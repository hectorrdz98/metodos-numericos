import numpy as np

colors = {
    'reset': '\033[0m',
    'green': '\033[32m',
    'yellow': '\033[93m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'bold': '\033[01m',
}

import os           
os.system('color')          # Activate color mode in terminal



# Datos de entrada
x       = [ 1.0, 1.3, 1.6, 1.9, 2.2 ]
fx      = [ 0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623 ] 
demals  = 7
xReq    = 1.5
fReq    = 0

# Número de x
n = len(x)

# Qs
Q = np.zeros([n, n])

# Q[i,0]
for i in range(n):
    Q[i][0] = fx[i]


# Calcular las Qs
for i in range(1, n):                   # i = Renglon
    for j in range(i, n):               # j = Columns
        Q[j][i] = ( ( ((xReq-x[j-i]) * Q[j][i-1]) - ((xReq-x[j]) * Q[j-1][i-1]) ) / (x[j] - x[j-i]) )

if demals:
    Q = np.round(Q, decimals=demals)

# Mostrar la matriz de Qs
print('\n{}{}Matriz de Qs{}\n'.format(
    colors['bold'], colors['blue'], colors['reset']
))
print(Q)

fReq = Q[n-1][n-1]

# Mostrar resultado
print('\n{}{}f({} {} {}): {}{}{}\n'.format(
    colors['bold'], colors['blue'], 
    colors['yellow'], xReq, colors['blue'], 
    colors['yellow'], fReq, colors['reset']
))
