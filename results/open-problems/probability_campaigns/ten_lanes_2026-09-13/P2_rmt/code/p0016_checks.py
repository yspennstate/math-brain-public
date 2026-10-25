"""Numerical audit of every step of the P0016 argument."""
import numpy as np, math, itertools
from math import comb, lgamma, log, sqrt, pi
rng = np.random.default_rng(20260913)

# ---- 1. g(d) = E[(1-rho^2)^{-1/2}] for rho = <u,v>, u,v iid uniform on S^d ----
def g(d):
    if d < 2: return math.inf
    return math.exp(lgamma((d-1)/2) + lgamma((d+1)/2) - 2*lgamma(d/2))
print("g(d) closed form vs Monte Carlo (u,v iid uniform on S^d in R^{d+1}):")
for d in [2,3,4,5,8,16,32,64]:
    n = 400000
    U = rng.standard_normal((n,d+1)); U /= np.linalg.norm(U,axis=1,keepdims=True)
    V = rng.standard_normal((n,d+1)); V /= np.linalg.norm(V,axis=1,keepdims=True)
    r = (U*V).sum(1)
    mc = np.mean(1.0/np.sqrt(np.maximum(1-r**2,1e-300)))
    print(f"  d={d:3d}  g={g(d):.6f}   MC={mc:.6f}   1+1/(4d)={1+1/(4*d):.6f}")

# ---- 2. the key sum S(m) = (1/N) sum_{d>=2} C(m,d)^2 g(d) ----
print("\nS(m) = (1/N) sum_{d>=2} C(m,d)^2 g(d)   [must be 1+o(1)]")
for m in [4,8,16,32,64,128,256,512]:
    N = comb(2*m,m)
    S = sum(comb(m,d)**2 * g(d) for d in range(2,m+1)) / N
    frac_d01 = (1 + m*m)/N
    print(f"  m={m:4d}  S={S:.8f}   S-1={S-1:.3e}   (1+m^2)/N={frac_d01:.3e}")

# ---- 3. Lemma check: law of rho_{TT'} for null directions of row subsets ----
print("\nLemma check: rho = <x_T,x_T'> vs uniform-sphere prediction, by d=|T\T'|")
def null_dir(rows):
    # unit null vector of a (k) x (k+1) matrix
    u,s,vt = np.linalg.svd(rows)
    return vt[-1]
for (M, d) in [(6,1),(6,2),(6,3),(6,5),(9,2),(9,4),(9,8)]:
    m = M-1
    if d > m: continue
    vals=[]
    for _ in range(4000):
        B = rng.standard_normal((2*m, M))
        T = list(range(m))
        Tp = list(range(m-d)) + list(range(m, m+d))
        xT = null_dir(B[T]); xTp = null_dir(B[Tp])
        vals.append(abs(xT@xTp))
    vals=np.array(vals)
    # predicted: |<u,v>| for u,v iid uniform on S^d
    n=200000
    U = rng.standard_normal((n,d+1)); U/=np.linalg.norm(U,axis=1,keepdims=True)
    V = rng.standard_normal((n,d+1)); V/=np.linalg.norm(V,axis=1,keepdims=True)
    pred = np.abs((U*V).sum(1))
    qs=[0.1,0.25,0.5,0.75,0.9]
    print(f"  M={M} d={d}: quantiles obs {np.round(np.quantile(vals,qs),4)}  pred {np.round(np.quantile(pred,qs),4)}")
