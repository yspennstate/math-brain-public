# -*- coding: utf-8 -*-
"""Among CORANK-1 symmetric +-1 matrices, what is the support size of the (unique up to scale,
   integer, primitive) kernel vector?  The conjectural asymptotic mechanism is support 2 (two equal
   or opposite columns).  Competing mechanisms have support 4, 6, ...: a support-2s kernel vector
   with +-1 coefficients costs binom(2s,s)4^{-s} per outside row (1/2 at s=1, 3/8 at s=2,
   5/16 at s=3, ...) but has ~n^{2s} choices, so at small n the larger supports win on counting.
   This measures where the crossover actually is."""
import numpy as np, sys, time
from fractions import Fraction
rng = np.random.default_rng(2718)

def kernel_vec_int(A, n):
    """exact primitive integer kernel vector for a corank-1 integer matrix, via fraction-free RREF"""
    from sympy import Matrix
    K = Matrix(A.tolist()).nullspace()
    if len(K) != 1: return None
    v = K[0]
    dens = [x.q for x in v]
    from math import gcd
    L = 1
    for d in dens: L = L*d//gcd(L,d)
    w = [int(x*L) for x in v]
    g = 0
    for x in w: g = gcd(g, abs(x))
    if g: w = [x//g for x in w]
    return w

for n in [8, 10, 12, 14]:
    tr = {8:60000, 10:120000, 12:300000, 14:900000}[n]
    hist = {}
    coef = {}
    done = 0; t0=time.time()
    while done < tr:
        m = min(40000, tr-done); done += m
        U = rng.integers(0,2,size=(m, n*(n+1)//2)).astype(np.int8)*2-1
        Ms = np.zeros((m,n,n), dtype=np.int8); t=0
        for i in range(n):
            for j in range(i,n):
                Ms[:,i,j]=U[:,t]; Ms[:,j,i]=U[:,t]; t+=1
        d = np.abs(np.linalg.det(Ms.astype(np.float64)))
        for r in np.nonzero(d < 0.5)[0]:
            A = Ms[r].astype(np.int64)
            s = np.linalg.svd(A.astype(float), compute_uv=False)
            if s[-2] < 1e-8: continue          # corank >= 2, skip
            w = kernel_vec_int(A, n)
            if w is None: continue
            sup = sum(1 for x in w if x != 0)
            hist[sup] = hist.get(sup,0)+1
            mx = max(abs(x) for x in w)
            coef[mx] = coef.get(mx,0)+1
    tot = sum(hist.values())
    print(f"n={n}  corank-1 matrices sampled: {tot} of {done} draws  ({time.time()-t0:.0f}s)")
    print(f"   support size of the kernel vector: " +
          ", ".join(f"{k}:{v} ({v/tot:.3f})" for k,v in sorted(hist.items())))
    print(f"   max |coefficient|:                " +
          ", ".join(f"{k}:{v} ({v/tot:.3f})" for k,v in sorted(coef.items())[:8]))
    sys.stdout.flush()
