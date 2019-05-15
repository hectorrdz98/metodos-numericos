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
# x       = [ 0, 1, 2, 3, 4 ]
# fx      = [ 1, 0.5403023, -0.4161468, -0.9899924, -0.6536436 ] 
x       = [12, 18, 24]
fx      = [148, 156, 147]
demals  = 7
xReq    = 0
fReq    = 0

# Número de x
n = len(x)

# Diferencias divididas
f = np.zeros([n, n])

# f [xi]
for i in range(n):
    f[i][0] = fx[i]


# Calcular las diferencias divididas
for i in range(1, n):                   # i = Renglon
    for j in range(i, n):               # j = Columna
        f[j][i] = ( (f[j][i-1] - f[j-1][i-1]) / (x[j] - x[j-i]) )

if demals:
    f = np.round(f, decimals=demals)

# Mostrar la matriz de Fs
print('\n{}{}Matriz de diferencias divididas{}\n'.format(
    colors['bold'], colors['blue'], colors['reset']
))
print(f)

# f de la diagonal, para el calculo de Newton
fNew = np.zeros([n])

for i in range(n):
    fNew[i] = f[i][i]

if demals:
    fNew = np.round(fNew, decimals=demals)

# Mostrar los elementos de la diagonal
print('\n{}{}Elementos de la diagonal{}\n'.format(
    colors['bold'], colors['purple'], colors['reset']
))
print(fNew)


# Obtener f( xReq )
PnX = ''
for k in range(n):
    Pi = 1
    for i in range(k):
        Pi *= ( xReq - x[i] )
    if demals:
        Pi = np.round(Pi, decimals=demals)
    preRes = (fNew[k] * Pi)
    if demals:
        preRes = np.round(preRes, decimals=demals)
    fReq += preRes
    PnX += '{} * {}'.format(fNew[k], Pi)
    if k < n-1:
        PnX += ' + '

if demals:
    fReq = np.round(fReq, decimals=demals)

print('\n{}{}P{}x = {}{}{}'.format(
    colors['bold'], colors['purple'], 
    n-1, colors['green'], PnX, colors['reset']
))
    


# Mostrar resultado
print('\n{}{}f({} {} {}): {}{}{}\n'.format(
    colors['bold'], colors['blue'], 
    colors['yellow'], xReq, colors['blue'], 
    colors['yellow'], fReq, colors['reset']
))
