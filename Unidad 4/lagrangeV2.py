import numpy as np

colors = {
    'reset': '\033[0m',
    'green': '\033[32m',
    'red': '\033[31m',
    'yellow': '\033[93m',
    'cyan': '\033[36m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'pink': '\033[95m',
    'bold': '\033[01m',
    'underline': '\033[04m',
}

import os           
os.system('color')          # Activate color mode in terminal


x = 2.5
Xs = np.array([ 0, 1, 2, 3, 4 ])
FXs = np.array([ 1, 0.5403023, -0.4161468, -0.9899924, -0.6536436 ])
decimals = 7
res = []

print('\n{}{}Partes del polinomio{}\n'.format(colors['bold'], colors['blue'], colors['reset']))

for k in range(len(Xs)):

    supPart = ''
    infPart = 1

    resP = 1

    for i in range(len(Xs)):
        if i != k:
            supPart += '(x-{})'.format(Xs[i])
            infPart *= (Xs[k] - Xs[i])
            resP *= (x-Xs[i])

    preRes = (FXs[k] / infPart) * resP
    
    if decimals:
        preRes = np.round(preRes, decimals=decimals)
    res.append(preRes)

    print('{} * ({} / {}) = {}'.format(
        FXs[k], supPart, infPart, res[k]
    ))
    print()


res = np.sum(res)
if decimals:
    res = np.round(res, decimals=decimals)

# Mostrar resultado
print('\n{}{}f({} {} {}): {}{}{}\n'.format(
    colors['bold'], colors['blue'], 
    colors['yellow'], x, colors['blue'], 
    colors['yellow'], res, colors['reset']
))