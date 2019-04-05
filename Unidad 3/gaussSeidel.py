import numpy as np
import re

fileName = 'examen2c.txt'
nRows = 0

with open(fileName) as file:
    for line in file:
        nRows += 1

original = np.zeros((nRows,nRows+1))

with open(fileName) as file:
    cont = 0
    for line in file:
        cont2 = 0
        if line[len(line) - 1] == '\n':
            line = line[0:len(line) - 1]
        datas = re.split(r'[^\S\n]', line)
        for data in datas:
            original[cont][cont2] = float(data)
            cont2 += 1
        cont += 1

T = np.zeros((nRows,nRows))
C = np.zeros((nRows,1))

print('\nMatriz aumentada:')
print(original)

for i in range(len(T)):
    for j in range(len(T)):
        if i != j:
            T[i][j] = -original[i][j] / original[i][i]

for i in range(len(T)):
    C[i] = original[i][nRows] / original[i][i]



# VALORES INICIALES

X0 = np.zeros((nRows,1))
decimales = None
tol = 0.0001
ite = 100



print('\nT:')
print(T)
print('\nC:')
print(C)

D = np.zeros((nRows,nRows))
L = np.zeros((nRows,nRows))
U = np.zeros((nRows,nRows))

for i in range(len(D)):
    for j in range(len(D)):
        if i == j:
            D[i][j] = original[i][j]
        if j < i:
            L[i][j] = original[i][j]
        if j > i:
            U[i][j] = original[i][j]

"""
print('\nD:')
print(D)
print('\nL:')
print(L)
print('\nU:')
print(U)
"""

print('\n\nResultados:')

XAux = X0

print('\nX0:')
print(XAux)

flag = False

for n in range(ite):
    XNorma = np.zeros_like(XAux)
    XNorma[:] = XAux[:]

    for row in range(len(T)):
        #print('T[{}]: {}'.format(row, T[row]))
        #XAux[row] = ( np.matmul(T[row], XAux) +  C[row])
        XAux[row] = np.matmul(T[row], XAux) +  C[row]
        if decimales:
            XAux[row] =  np.around(XAux[row], decimals=decimales)

    print('\nX{}:'.format(n+1))
    print(XAux)

    XNorma = XAux - XNorma
    # print('\nXNorma{}:'.format(n+1))
    # print(XNorma)
    XNorma = np.absolute(XNorma)
    # print('\nXNormaAbs{}:'.format(n+1))
    # print(XNorma)

    NormaLInf = np.amax(XNorma)
    print('\nNormaLInf{}: {}'.format(n+1, NormaLInf))

    if NormaLInf <= tol:
        flag = True
        print('\n¡Ya llegamos a la tol ({}) con ite={}!'.format(tol, n+1))
        break    

if not flag:
    print('\nNo se llegó a la tol ({}) con {} iteraciones...'.format(tol, ite))

print('\nX:')
print(XAux)