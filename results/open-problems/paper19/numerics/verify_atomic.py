"""
Validate the nonzero-alphabet quotient specialization of the deterministic
finite-alphabet projective-pair obstruction (II.C-proj): for a finite alphabet
S subset K^* with q = |S/S| (number of distinct ratios), every
A in S^{N x m} with N >= q(m-1)+1 and m>=2 has a singular m-row submatrix.
Check: at the threshold N0=q(m-1)+1 the fraction of random S-matrices with a singular m-minor is 1.0;
below N0 the random sample may show full-spark S-frames in small cases, but this script is
not an exhaustive below-threshold sharpness proof.
Run: python verify_atomic.py
"""
import numpy as np
from itertools import combinations
from fractions import Fraction
rng=np.random.default_rng(20260628)

def qsize(S):
    ratios=set()
    for a in S:
        for b in S:
            ratios.add(Fraction(a,b))
    return len(ratios)

def has_singular_minor(A,m,tol=1e-9):
    N=A.shape[0]
    for S in combinations(range(N),m):
        if abs(np.linalg.det(A[list(S)].astype(float)))<tol:
            return True
    return False

def frac_singular(S,m,N,trials):
    cnt=0
    for _ in range(trials):
        A=rng.choice(S,size=(N,m))
        if has_singular_minor(A,m): cnt+=1
    return cnt/trials

for S,name in [([1,-1],"sign {+-1}  (q=2)"), ([1,2],"{1,2}  (q=3)"), ([1,2,4],"{1,2,4}")]:
    q=qsize(S)
    print(f"alphabet {name}: q=|S/S|={q}")
    for m in [2,3,4]:
        N0=q*(m-1)+1
        f_at=frac_singular(S,m,N0,400)
        f_below=frac_singular(S,m,N0-1,2000) if N0-1>=m else float('nan')
        print(f"   m={m}: threshold N0={N0}: frac singular={f_at:.3f}  (theory 1.000);"
              f"  at N0-1={N0-1}: sampled frac singular={f_below:.3f}")
print("DONE.  frac=1.000 at N0 confirms the obstruction in these samples; below-threshold rows are exploratory.")
