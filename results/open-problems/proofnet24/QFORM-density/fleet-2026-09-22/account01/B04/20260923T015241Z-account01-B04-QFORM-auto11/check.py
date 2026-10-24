from fractions import Fraction
from itertools import combinations
from math import e
import numpy as np


def sylvester(n):
    H=np.array([[1]],dtype=int)
    while H.shape[0]<n:
        H=np.block([[H,H],[H,-H]])
    return H

n=16
H=sylvester(n)
U=H[:,:3]/4.0
M=np.diag([1.0,1.0,-1.0])
A=U@M@U.T

triples=list(combinations(range(n),3))
weights={}
for S in triples:
    w=float(np.linalg.det(U[list(S),:])**2)
    if w>1e-12:
        weights[S]=w

assert len(weights)==256
assert max(abs(w-1/256) for w in weights.values())<1e-12
assert abs(sum(weights.values())-1)<1e-12

ordered_disjoint=sum(
    1 for S in weights for T in weights if set(S).isdisjoint(T)
)
assert ordered_disjoint==256*135
D=Fraction(ordered_disjoint,256**2)
assert D==Fraction(135,256)

vals=np.linalg.eigvalsh(A)
assert np.allclose(vals[-2:],[1,1],atol=1e-12)
assert abs(vals[0]+1)<1e-12
assert np.count_nonzero(np.abs(vals)>1e-10)==3
assert set(np.round(A.flatten(),12))=={-0.0625,0.0625,0.1875}

B=A[:8,8:]
s=np.linalg.svd(B,compute_uv=False)
assert np.allclose(s[:3],[0.5,0.5,0.5],atol=1e-12)
assert max(abs(x) for x in s[3:])<1e-12
E3=(s[0]*s[1]*s[2])**2
assert abs(E3-1/64)<1e-12

print('nonzero_triples=',len(weights))
print('each_weight=',Fraction(1,256))
print('ordered_disjoint_pairs=',ordered_disjoint)
print('d(U)=',D,'=',float(D))
print('row_leverage=',3/16)
print('A_entry_values=',sorted(set(np.round(A.flatten(),12))))
print('nonzero_spectrum=',[-1,1,1])
print('explicit_cut_singular_values=',s[:3].tolist())
print('explicit_cut_E3=',E3)
print('general_d_bound_constant=',6*e*float(D)**(-1/6))
print('explicit_cut_constant=',6*e)
