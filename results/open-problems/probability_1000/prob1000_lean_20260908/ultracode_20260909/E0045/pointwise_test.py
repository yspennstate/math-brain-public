# Test the pointwise (in s) strengthening of the endpoint conjecture:
#   P(min_i |X_i| > s)  >=  prod_i P(|Y_i| > s)   for X = T Y, Y ~ N(0, diag(sig)).
# P(min|X_i|>s) = sum over sign vectors eps of P(eps_i X_i > s for all i) = sum of N-variate normal CDFs.
import numpy as np, itertools, sys
from scipy.stats import multivariate_normal, norm
from scipy.linalg import expm
rng = np.random.default_rng(1)

def p_min_gt(C, s):
    N = len(C); tot = 0.0
    for eps in itertools.product([1,-1], repeat=N):
        e = np.array(eps, float)
        Ce = C * np.outer(e, e)
        # P(eps_i X_i > s all i) = P(V_i > s) with V = diag(eps) X ~ N(0,Ce) = P(-V_i < -s) = cdf(-s) 
        tot += multivariate_normal.cdf(-s*np.ones(N), mean=np.zeros(N), cov=Ce, allow_singular=True, abseps=1e-9, releps=1e-9)
    return tot

def p_eig(sig, s):
    return np.prod(2*norm.sf(s/np.sqrt(sig)))

worst = 1e9
for trial in range(30):
    N = 3 if trial < 20 else 4
    sig = np.sort(rng.uniform(0.05, 1, N))[::-1]
    A = rng.standard_normal((N,N)); A = (A - A.T)*rng.uniform(0.2,1.5)
    T = expm(A); C = T @ np.diag(sig) @ T.T
    for s in [0.05, 0.1, 0.2, 0.35, 0.5, 0.8, 1.2, 1.8]:
        a = p_min_gt(C, s); b = p_eig(sig, s)
        d = a - b
        if d < worst: worst = d; print(f"new worst: N={N} sig={np.round(sig,3)} s={s} P_T={a:.6g} P_eig={b:.6g} diff={d:.3e}", flush=True)
print("worst diff (should be >= 0 if pointwise claim holds):", worst)
# van Handel-style structured T at the eigen-degenerate boundary: sig=(1,1,eps), T = rows orthonormal mixing e3 uniformly
for eps in [0.5, 0.1, 0.01]:
    sig = np.array([1.0,1.0,eps])
    u = np.ones(3)/np.sqrt(3); T = np.linalg.qr(np.column_stack([rng.standard_normal((3,2)), u]))[0]
    T = T.T  # rows: last row is +-u
    C = T @ np.diag(sig) @ T.T
    for s in [0.05,0.2,0.5,1.0]:
        print(f"eps={eps} s={s} P_T={p_min_gt(C,s):.6g} P_eig={p_eig(sig,s):.6g}", flush=True)
