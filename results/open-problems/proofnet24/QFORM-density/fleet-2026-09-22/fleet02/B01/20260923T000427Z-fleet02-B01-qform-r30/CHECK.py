import itertools, math
import numpy as np

m=8
n=2*m+1
A=np.zeros((n,n))
a=1/math.sqrt(m)
for j in range(1,m+1):
    A[0,j]=A[j,0]=a
for j in range(m+1,2*m+1):
    for k in range(m+1,2*m+1):
        A[j,k]=1/m

vals=np.linalg.eigvalsh(A)
nz=vals[np.abs(vals)>1e-10]
max_diag=float(np.max(np.abs(np.diag(A))))
max_pair=0.0
for i in range(n):
    for j in range(i+1,n):
        max_pair=max(max_pair,abs(float(np.linalg.det(A[np.ix_([i,j],[i,j])] ))))

max_rank=0
bad=0
for mask in range(1,(1<<n)-1):
    I=[i for i in range(n) if (mask>>i)&1]
    J=[i for i in range(n) if not ((mask>>i)&1)]
    r=int(np.linalg.matrix_rank(A[np.ix_(I,J)],tol=1e-10))
    max_rank=max(max_rank,r)
    if r>2:
        bad+=1
        break

print('m',m)
print('nonzero eigenvalues',nz)
print('max |diag|',max_diag)
print('max |2x2 principal det|',max_pair)
print('max cross rank',max_rank,'bad',bad)
print('mixed-hub constant',3*2**(4/3))
print('partner power prefactor',11.021*2**0.1)
assert np.allclose(nz,[-1,1,1],atol=1e-10)
assert abs(max_diag-1/m)<1e-12
assert abs(max_pair-1/m)<1e-12
assert max_rank<=2 and bad==0
print('STATUS=PASS')
