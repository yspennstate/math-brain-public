"""
T2 sanity check: support-minimised smallest singular value large-deviation rate.

Conjecture (paper22 B.2/B.4): for A an N x N Ginibre (real d_F=1 / complex d_F=2)
with entries of unit variance (real) resp. E|a|^2 = 1 (complex),
    rho_N := -(1/N) log min_{|S|=|T|=alpha N} sigma_min(A[T,S])   -->   2 H(alpha)/d_F
where H(alpha) = -alpha log alpha - (1-alpha) log(1-alpha)  (natural log).

Proved bracket: H(alpha)/d_F <= rho <= 2 H(alpha)/d_F.

We enumerate all pairs (S,T) for small N (alpha=1/2) and track the trend of rho_N
toward the conjectured 2H/d_F and away from the lower bracket H/d_F.
Finite-N values sit below the limit (polynomial sqrt(n) prefactors + pre-asymptotic
support entropy), so we look for a monotone climb through the bracket, not equality.
"""
import numpy as np
from itertools import combinations
import math

def min_sv_over_supports(A, n):
    N = A.shape[0]
    subsets = list(combinations(range(N), n))
    best = np.inf
    for T in subsets:
        rowsub = A[np.ix_(T, range(N))]
        for S in subsets:
            M = rowsub[:, S]
            s = np.linalg.svd(M, compute_uv=False)[-1]
            if s < best:
                best = s
    return best

def run(N, field='real', reps=8, seed=0):
    rng = np.random.default_rng(seed)
    n = N // 2
    alpha = n / N
    H = -alpha*math.log(alpha) - (1-alpha)*math.log(1-alpha)
    d_F = 1 if field == 'real' else 2
    rhos = []
    for _ in range(reps):
        if field == 'real':
            A = rng.standard_normal((N, N))
        else:
            A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N))) / math.sqrt(2)
        m = min_sv_over_supports(A, n)
        rhos.append(-math.log(m) / N)
    rhos = np.array(rhos)
    print(f"  N={N:2d} n={n} {field:7s} d_F={d_F}: rho_N = {rhos.mean():.4f} +/- {rhos.std()/math.sqrt(reps):.4f}"
          f"   [lower bracket H/d_F={H/d_F:.4f}, conjecture 2H/d_F={2*H/d_F:.4f}]")
    return rhos.mean(), H/d_F, 2*H/d_F

if __name__ == "__main__":
    print("REAL:")
    for N in (6, 8, 10, 12):
        reps = 16 if N <= 8 else (8 if N == 10 else 3)
        run(N, 'real', reps=reps, seed=100+N)
    print("COMPLEX:")
    for N in (6, 8, 10):
        reps = 16 if N <= 8 else 8
        run(N, 'complex', reps=reps, seed=200+N)
