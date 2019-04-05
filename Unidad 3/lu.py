import math
import numpy as np

a = np.array([[-20,3,20], [10,1,-5], [5,3,5]])

l = np.zeros(a.shape)
u = np.zeros(a.shape)

tl = np.array([[1,0,0], [-0.5,1,0], [-0.25,1.5,1]])
tu = np.array([[-20,3,20], [0,2.5,5], [0,0,2.5]])

for i in range(a.shape[0]):
    print('\nComenzamos con u[{}][j]:'.format(i))
    for j in range(a.shape[1]):
        listed = [ (tl[i][k]*tu[k][j]) for k in range(i) ]
        u[i][j] = a[i][j] - sum(listed)
    #    print('Ahora u[{}][{}]: {}'.format(i,j,u[i][j]))
        print(listed, ': ', sum(listed))
    
    print('\nSeguimos con l[j][{}]:'.format(i))
    for j in range(a.shape[1]):
        listed = [ (tl[j][k] * tu[k][j]) for k in range(i) ]
        print(listed, sum(listed))
        l[j][i] = ( a[j][i] - sum(listed) ) / tu[i][i]
    #    print('Ahora l[{}][{}]: {}'.format(j,i,l[j][i]))
    
    
print()
print('L:\n',l)
print()
print('U:\n',u)