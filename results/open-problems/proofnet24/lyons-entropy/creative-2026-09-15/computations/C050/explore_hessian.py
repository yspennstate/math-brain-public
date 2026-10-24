"""Explore the finite marked-replica matrix certificate; exact data are rational."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
n = 3
K = sp.Matrix([[sp.Rational(13,20) if i == j else -sp.Rational(3,10)
                for j in range(n)] for i in range(n)])
basis = []
labels = []
for i in range(n):
    E = sp.zeros(n); E[i,i] = 1
    basis.append(E); labels.append(f'd{i}')
for i in range(n):
    for j in range(i+1,n):
        E = sp.zeros(n); E[i,j] = E[j,i] = 1
        basis.append(E); labels.append(f're{i}{j}')
for i in range(n):
    for j in range(i+1,n):
        E = sp.zeros(n); E[i,j] = sp.I; E[j,i] = -sp.I
        basis.append(E); labels.append(f'im{i}{j}')

atoms = []
for bits in product((0,1), repeat=n):
    M = sp.Matrix.hstack(*[(K if bit else sp.eye(n)-K)[:,j]
                          for j,bit in enumerate(bits)])
    p = M.det()
    R = [M.inv()*sp.Matrix.hstack(*[(E if bit else -E)[:,j]
                                  for j,bit in enumerate(bits)]) for E in basis]
    v = sp.Matrix([sp.simplify(p*X.trace()) for X in R])
    B = sp.Matrix([[sp.simplify(p*(X.trace()*Y.trace()-(X*Y).trace()))
                    for Y in R] for X in R])
    mu = sp.prod(sp.Rational(13,20) if bit else sp.Rational(7,20) for bit in bits)
    atoms.append((bits,p,mu,v,B))

assert sum((v for _,p,mu,v,B in atoms),sp.zeros(9,1)) == sp.zeros(9,1)
assert sum((B for _,p,mu,v,B in atoms),sp.zeros(9,9)) == sp.zeros(9,9)
assert all(sum((B for bits,p,mu,v,B in atoms if bits[i]),sp.zeros(9,9)) == sp.zeros(9,9)
           for i in range(n))
data = {'labels':labels,'atoms':[{'bits':bits,'p':str(p),'mu':str(mu),
          'v':[str(z) for z in v], 'B':[[str(z) for z in row] for row in B.tolist()]}
         for bits,p,mu,v,B in atoms]}
(ROOT/'hessian_jets.json').write_text(json.dumps(data,indent=2)+'\n')

H = np.zeros((9,9))
for bits,p,mu,v,B in atoms:
    vf = np.array(v,float).reshape(-1)
    H += np.outer(vf,vf)/float(p)+np.array(B,float)*np.log(float(p))
print('eigenvalues of -H',np.linalg.eigvalsh(H))
for N in [6,12,24,32,40,48,64,80,100,128,160,240]:
    L = np.zeros((9,9))
    for bits,p,mu,v,B in atoms:
        u = float(1-p/(2*mu)); x = 1-u
        vf = np.array(v,float).reshape(-1); Bf=np.array(B,float)
        S = sum(u**j/j for j in range(1,N+1))
        e = u**(N+1)/((N+1)*x)
        D = np.diag(np.abs(Bf).sum(axis=1))
        L += np.outer(vf,vf)/float(p)*(1-u**N)-Bf*S-e*D
    print(N,'certified matrix least eigenvalue diagnostic',np.linalg.eigvalsh(L)[0])
