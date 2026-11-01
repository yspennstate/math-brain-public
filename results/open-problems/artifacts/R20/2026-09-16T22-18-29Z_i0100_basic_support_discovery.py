#!/usr/bin/env python3
"""
DISCOVERY ONLY — NOT AN EXACT CERTIFICATE.

R20 / I0100 numerical exploration for the projected-simplex/basic-support
formulation of Randomstrasse Conjecture 26.  It solves the full real moment LP
with SciPy/HiGHS for the already-exactly-certified primes 181, 241, 421.  The
purpose is only to inspect symmetry-breaking basic supports and test the
Fourier-minor formula numerically.  No finite claim in the R20 report relies
on this output as proof.
"""
import numpy as np
import sympy as sp
from scipy.optimize import linprog

def local_sets(p):
    n=(p-1)//2
    g=int(sp.primitive_root(p))
    alpha=pow(g,2,p)
    Q={x*x % p for x in range(1,p)}
    vals=[pow(alpha,j,p) for j in range(n)]
    S=[d for d in range(1,n) if (vals[d]-1)%p in Q]
    N=[d for d in range(1,n) if d not in S]
    return n,S,N

def solve(p):
    n,S,N=local_sets(p)
    seen=set(); reps=[]
    for s in S:
        if s in seen: continue
        reps.append(s); seen.add(s); seen.add((-s)%n)
    cols=np.arange(n)
    A=[np.ones(n)]; b=[1.0]
    for s in reps:
        row=np.exp(2j*np.pi*s*cols/n)
        A.append(row.real); b.append(0.0)
        if np.max(np.abs(row.imag))>1e-12:
            A.append(row.imag); b.append(0.0)
    c=np.zeros(n); c[0]=-1.0
    res=linprog(c,A_eq=np.array(A),b_eq=np.array(b),
                bounds=(0,None),method="highs")
    assert res.success
    supp=np.where(res.x>1e-8)[0]
    d=len(S)
    print(f"p={p} n={n} d={d} nu0={res.x[0]:.15g} "
          f"theta={1/res.x[0]:.15g} support_size={len(supp)}")
    print("support =",supp.tolist())
    if len(supp)==d+1 and 0 in supp:
        B=[int(m) for m in supp if m!=0]
        z=np.exp(2j*np.pi/n)
        W=np.array([[z**(s*m) for m in B] for s in S],dtype=complex)
        T=1-np.ones(d)@np.linalg.solve(W,np.ones(d))
        print(f"basic_minor_T={T.real:.15g} imag={T.imag:.3e} "
              f"error={abs(T.real-1/res.x[0]):.3e}")
    else:
        print("basic_minor_T=DEGENERATE_SUPPORT (square formula not invoked)")
    print()

for p in (181,241,421):
    solve(p)

print("DISCOVERY_ONLY=PASS")
print("NO_EXACT_CERTIFICATE_CLAIM")
