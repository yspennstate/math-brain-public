import math
import numpy as np
from scipy.special import beta

C1=math.sqrt(math.e)*2**(-3/4)*beta(1/4,1/4)
C3=math.sqrt(math.e)/2*beta(1/4,1/8)
print(f"C1 = {C1:.17f}")
print(f"C3 = {C3:.17f}")

A=np.array([[1,1,0,1,0],
            [1,0,0,1,0],
            [0,0,0,0,1],
            [1,1,0,0,0],
            [0,0,1,0,0]],dtype=float)
print("falsifier_eigenvalues =",np.array2string(np.linalg.eigvalsh(A),precision=12))
I=[1,2]; J=[3,4]
C=A[np.ix_(I,J)]
bI=A[I,0][:,None]
bJ=A[0,J][None,:]
Cp=C-bI@bJ/A[0,0]
print("pre_singular_values =",np.linalg.svd(C,compute_uv=False))
print("post_singular_values =",np.linalg.svd(Cp,compute_uv=False))

for m in range(3,11):
    p=(m+1)//2; q=m//2
    s=math.sqrt(p*q)/m
    rho=1/p
    bd=C1*s**(-0.5)
    print(f"bank m={m:2d} p={p} q={q} sigma={s:.12f} rho={rho:.12f} bound={bd:.12f}")

assert np.sum(np.abs(np.linalg.eigvalsh(A))>=1-1e-10)>=3
assert np.linalg.matrix_rank(C)==2 and np.linalg.matrix_rank(Cp)==1
assert C1<7.271 and C3<9.500
print("QFORM_B05_CROSS_RIESZ_PASS")
