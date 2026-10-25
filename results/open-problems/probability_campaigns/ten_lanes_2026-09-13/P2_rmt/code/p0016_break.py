"""Break tests for the P0016 claims."""
import numpy as np, itertools, math
from math import comb, log, sqrt, pi
rng = np.random.default_rng(4242)

# ---- B1. is the min really attained at |S| = M?  (monotonicity sanity) ----
bad = 0
for _ in range(300):
    M = 4; A = rng.standard_normal((2*M-1, M))
    mM  = min(np.linalg.svd(A[list(S)],compute_uv=False)[-1] for S in itertools.combinations(range(2*M-1),M))
    mM1 = min(np.linalg.svd(A[list(S)],compute_uv=False)[-1] for S in itertools.combinations(range(2*M-1),M+1))
    if mM1 < mM - 1e-12: bad += 1
print("B1 monotonicity violations (should be 0):", bad)

# ---- B2. the one-row-left-out upper bound really bounds omega ----
viol=0
for _ in range(200):
    M=5; A=rng.standard_normal((2*M-1,M)); B=A[:2*M-2]; g=A[-1]
    om = min(np.linalg.svd(A[list(S)],compute_uv=False)[-1] for S in itertools.combinations(range(2*M-1),M))
    best=np.inf
    for T in itertools.combinations(range(2*M-2), M-1):
        u,s,vt = np.linalg.svd(B[list(T)]); x = vt[-1]
        best=min(best, abs(g@x))
    if om > best + 1e-12: viol+=1
print("B2 omega <= min_T |<g,x_T>| violations (should be 0):", viol)

# ---- B3. full distribution of omega*4^M vs Exponential(mean 2 sqrt(pi)) ----
print("\nB3  distribution of omega*4^M   (Exp prediction: P(>s)=exp(-s/(2 sqrt pi)), mean 3.545)")
for M in [6,7,8]:
    tr = {6:4000,7:1500,8:700}[M]
    v=[]
    for _ in range(tr):
        A=rng.standard_normal((2*M-1,M))
        v.append(min(np.linalg.svd(A[list(S)],compute_uv=False)[-1] for S in itertools.combinations(range(2*M-1),M)))
    v=np.array(v)*4**M
    qs=[0.1,0.25,0.5,0.75,0.9]
    lam = 1/(2*sqrt(pi))
    pred=[-log(1-q)/lam for q in qs]
    print(f"  M={M} n={tr}  mean={v.mean():.3f} (pred 3.545)   quantiles {np.round(np.quantile(v,qs),3)}  pred {np.round(pred,3)}")
    # finite-M exact-rate version: lambda_M = C(2M-1,M)*kappa_M, kappa_M measured
    G = rng.standard_normal((200000,M,M)); s=np.linalg.svd(G,compute_uv=False)[:,-1]
    h=0.02/sqrt(M); kap = 2*np.mean(s<=h/2)/(h/2)-np.mean(s<=h)/h
    lamM = comb(2*M-1,M)*kap*4**-M
    pred2=[-log(1-q)/lamM for q in qs]
    print(f"        finite-M rate lambda_M={lamM:.4f} (limit {1/(2*sqrt(pi)):.4f})  pred {np.round(pred2,3)}")
