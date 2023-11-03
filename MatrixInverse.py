import numpy as np
import scipy.linalg as la

matrix = np.array([[1,2,-3,4],[4,8,12,-8],[2,3,2,1],[-3,-1,1,-4]])

#print(np.linalg.inv(matrix))
P,L,U = la.lu(matrix)

#print(f'Permutation {P}')
#print(f'Diagonal M {L')
#print(f'Upper T {U}')

matrix = np.array([[0,1],[1,0]])

print(f'inverse for matrix {la.inv(matrix)}')
print(f'LU for matrix {la.lu(matrix)}')


## LU automatically does permutation if there is 0 pivot during gaussian elimination