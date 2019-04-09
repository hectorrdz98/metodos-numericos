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


x = 1.5
Xs = np.array([ 1.0, 1.3, 1.6, 1.9, 2.2 ])
FXs = np.array([ 0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623 ])
decimals = 7
res = np.zeros_like(Xs)

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
    res[k] = preRes

    print('{} * ({} / {}) = {}'.format(
        FXs[k], supPart, infPart, res[k]
    ))


res = np.sum(res)
if decimals:
    res = np.round(res, decimals=decimals)

# Mostrar resultado
print('\n{}{}f({} {} {}): {}{}{}\n'.format(
    colors['bold'], colors['blue'], 
    colors['yellow'], x, colors['blue'], 
    colors['yellow'], res, colors['reset']
))