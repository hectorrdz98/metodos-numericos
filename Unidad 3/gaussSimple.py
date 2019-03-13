import numpy as np
import re

fileName = 'cosa1.txt'
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
        #print(datas)
        for data in datas:
            original[cont][cont2] = float(data)
            cont2 += 1
        cont += 1

print()
print('Original:')
print(original)
print()

coefs = original

for i in range(0, nRows-1):
    for n in range(i+1, nRows):
        m = (-coefs[n][i] / coefs[i][i])
        #print('coefs[{}][{}]: {}, coefs[{}][{}]: {}'.format(n, i, coefs[n][i], i, i, coefs[i][i]))
        #print('m: {}'.format(m))
        cont = 0
        for coef in coefs[n]:
            coefs[n][cont] = (m * coefs[i][cont]) + coef
            cont += 1
    print(coefs)
    print()

# Resolución

values = np.zeros(nRows) # Results

cont = nRows - 1
values[cont] = coefs[cont][cont+1] / coefs[cont][cont] # último
#print('values[{}]: {}'.format(cont, values[cont]))

cont2 = cont
for n in reversed(range(0, cont)):
    partialAns = 0
    nSums = nRows - (n+1)
    for i in range(nSums):
    #    print('coefs[{}][{}]: {}, values[{}]: {}'.format(
    #        n, cont-i, coefs[n][cont-i], (cont-i), values[cont-i]
    #    ))
        partialAns += (coefs[n][cont-i] * values[cont-i])
    #    print('partialAns: {}'.format(partialAns))

    actual = coefs[n][cont2-1]
    last = coefs[n][nRows]

    #print('actual {}, last {}'.format(actual, last))

    values[n] = (last - partialAns) / actual
    #print('values[{}]: {}'.format(n, values[n]))
    cont2 -= 1

results = []

cont = 1
for value in values:
    results.append('x{}= {}'.format(cont, value))
    cont += 1

print('Resultados:')

for result in results:
    print(result)

print('\nMatriz de resultados: {}'.format(values))
