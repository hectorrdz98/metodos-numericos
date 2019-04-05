import numpy as np
import math

textColors = {
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



"""Xs = np.array([2, 2.5, 4])
decimals = 3

def f(x):
    return 1/x
"""

Xs = np.array([1, 2, 4])
decimals = 3

def f(x):
    return math.exp(x)

PParts = []
LagrangeFormat = []

print('\n{}{}Partes del polinomio{}\n'.format(textColors['bold'], textColors['blue'], textColors['reset']))

for k in range(len(Xs)):

    supPart = ''
    supPol = [0, 0, 1]
    infPart = 1

    for i in range(len(Xs)):
        if i != k:
            supPart += '(x-{})'.format(Xs[i])
            infPart *= (Xs[k] - Xs[i])
            supPol[0] += 1
            supPol[1] += -(Xs[i])
            supPol[2] *= -(Xs[i])

    print('{} * ({} / {})'.format(
        f(Xs[k]), supPart, infPart
    ))

    PParts.append('{} * (x^{} + {}x + {} / {})'.format(
        f(Xs[k]), supPol[0], supPol[1], supPol[2], infPart
    ))

    LagrangeFormat.append([
        f(Xs[k]), supPol[0], supPol[1], supPol[2], infPart
    ])

    print(PParts[k])
    print()

LagrangeFormatAux = LagrangeFormat

PxV1 = ''
for part in PParts:
    PxV1 += '[ ' + part + ' ]'
    if part != PParts[len(PParts)-1]:
        PxV1 += ' + '

print('\n{}{}Polinomio de Lagrange{}\n'.format(textColors['bold'], textColors['green'], textColors['reset']))

print('P{}(x)= {}'.format(len(Xs)-1, PxV1))


PxV2 = []
for LFPart in LagrangeFormat:
    PxV2.append([
        LFPart[0] * 1 / LFPart[4], LFPart[0] * LFPart[2] / LFPart[4], LFPart[0] * LFPart[3] / LFPart[4]
    ])

PxP2 = np.array(PxV2)

# Ya con operaciones, pero en matriz
print()
print(PxP2)

# Ya realizada la suma de x^2 con x^2 etc...
PxP2 = PxP2.sum(axis=0)
print()
print(PxP2)

Lagrange = ''
for n in reversed(range(len(Xs))):
    if not decimals:
        partial = PxP2[len(Xs) - 1 - n]
    else:
        partial = round(PxP2[len(Xs) - 1 - n], decimals)
    if n > 1:
        Lagrange += '{}x^{}'.format( partial, n )
    elif n == 1:
        Lagrange += '{}x'.format( partial )
    else:
        Lagrange += '{}'.format( partial )
    if n > 0:
        Lagrange += ' + '

print()
print('{}{}{}{}'.format(textColors['bold'], textColors['green'], Lagrange, textColors['reset']))