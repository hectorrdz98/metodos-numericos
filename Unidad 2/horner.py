import math

coef = '2 0 -3 3 -4'
x0 = -2
n = 2
tol = 0.0001

def division(strCoef, num):
    matrizCoef = strCoef.split(' ')
    actual = float(matrizCoef[0])
    res = str(actual)
    res2 = 0
    for j in range(len(matrizCoef)-1):
        actual = actual*x0 + float(matrizCoef[j+1])
        if j < len(matrizCoef)-2:
            res += ' {}'.format(actual)
        else:
            res2 = actual
    return {
        'strRes': res,
        'res': res2
    }

print('')

for i in range(n):
    pDiv = division(coef, x0)
    pprimeDiv = division(pDiv['strRes'], pDiv['res'])
    x1 = x0 - (pDiv['res'] / pprimeDiv['res'])
    print('Vamos en {} con x0={} y x1={}'.format(i+1, x0, x1))
    x0 = x1

print('\nLlegamos a {} con {} ite'.format(x0, n))