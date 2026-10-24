from itertools import combinations
from math import pi, sqrt

A = [
    [0,0,1,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,1,0,0],
]

def det(M):
    n=len(M)
    if n==0: return 1
    if n==1: return M[0][0]
    return sum(((-1)**j)*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(n))

def mmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

I4=[[int(i==j) for j in range(4)] for i in range(4)]
assert mmul(A,A)==I4               # eigenvalues are all +/-1
assert det(A)==1                   # invertible 4x4 block, sigma_min=1 since A^2=I
for I in combinations(range(4),3):
    M=[[A[i][j] for j in I] for i in I]
    assert det(M)==0               # every principal 3x3 block is singular

C3=2*pi+3*sqrt(3)
C4=4*pi+8
assert C3 < C4 < 20.57
print('PASS')
print('C3 =', C3)
print('C4 =', C4)
