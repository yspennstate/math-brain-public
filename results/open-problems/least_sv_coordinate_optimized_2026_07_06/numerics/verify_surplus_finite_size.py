"""
Surplus r=1 check: exhaustive two-sided min over (n+1) x n submatrices vs the
first-moment prediction and the conjectured constant 2H(alpha)/(d_F(r+1)).

M_N^(1) = min_{|T|=n+1, |S|=n} sigma_min(A[T,S]),  rho = -(1/N) log M_N^(1).
First-moment scale t*: C(N,n+1)*C(N,n)*c_cal*(sqrt(n) t)^{d_F(r+1)} = 1,
c_cal calibrated by MC on a single (n+1) x n Gaussian block.
Target constants (alpha=1/2): real 2H/2 = 0.6931; complex 2H/4 = 0.3466.
"""
import numpy as np, math
from itertools import combinations
from math import lgamma, log

def logC(N, k): return lgamma(N+1)-lgamma(k+1)-lgamma(N-k+1)

def gauss(shape, cplx, rng):
    if cplx: return (rng.standard_normal(shape)+1j*rng.standard_normal(shape))/math.sqrt(2)
    return rng.standard_normal(shape)

def exhaustive_min_surplus(A, n):
    N = A.shape[0]
    Ts = list(combinations(range(N), n+1)); Ss = list(combinations(range(N), n))
    best = np.inf
    for T in Ts:
        RT = A[list(T), :]
        for S in Ss:
            s = np.linalg.svd(RT[:, list(S)], compute_uv=False)[-1]
            if s < best: best = s
    return best

def calibrate(n, cplx, rng, reps=150000):
    dF = 2 if cplx else 1; expo = dF*2   # d_F(r+1), r=1
    t = 0.15/math.sqrt(n)
    hits = 0; B = 15000; done = 0
    while done < reps:
        b = min(B, reps-done); done += b
        G = gauss((b, n+1, n), cplx, rng)
        s = np.linalg.svd(G, compute_uv=False)[:, -1]
        hits += int((s <= t).sum())
    p = hits/reps
    return p/((math.sqrt(n)*t)**expo)

def run(field):
    cplx = (field=='C'); dF = 2 if cplx else 1; expo = dF*2
    tgt = 2*math.log(2)/expo
    print(f"=== field {field}: target 2H/(d_F(r+1)) = {tgt:.4f} ===", flush=True)
    for N in (8, 10, 12):
        n = N//2
        if N == 12 and cplx: break
        rng = np.random.default_rng(3000+N+(50 if cplx else 0))
        c = calibrate(n, cplx, rng)
        log_t = -(logC(N,n)+logC(N,n+1)+log(max(c,1e-9))+expo*0.5*log(n))/expo
        rho_pred = -log_t/N
        reps = 10 if N <= 10 else 3
        ms = []
        for _ in range(reps):
            A = gauss((N,N), cplx, rng)
            ms.append(-log(exhaustive_min_surplus(A,n))/N)
        ms = np.array(ms)
        print(f"  N={N:2d} n={n}: rho_meas={ms.mean():.4f}+/-{ms.std()/math.sqrt(reps):.4f}"
              f"  rho_pred={rho_pred:.4f}  [c_cal={c:.3f}]", flush=True)

if __name__ == "__main__":
    run('R'); run('C')
