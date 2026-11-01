"""E0045 (Mallat-Zeitouni, Bandeira Open Problem 1.1): g ~ N(0, Sigma) in R^p, d < p. For an orthonormal basis V,
Gamma_V = max over d-subsets S of sum_{i in S} (v_i^T g)^2. Conjecture: E Gamma_V is maximised by the eigenbasis of Sigma.
Known for d = 1. Test d = 2 (and 3) at p = 3, 4, 5 by Monte Carlo with common random numbers and a random-restart optimiser over SO(p).
Since sum of all squared projections is |g|^2 for any orthonormal basis, E Gamma_V = tr Sigma - E[sum of the (p-d) smallest squared projections]."""
import numpy as np, sys
from scipy.optimize import minimize
from scipy.linalg import expm
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
def skew(x, p):
    A = np.zeros((p, p)); iu = np.triu_indices(p, 1); A[iu] = x; return A - A.T
for p, d in [(3, 2), (4, 2), (4, 3), (5, 2)]:
    lam = np.sort(rng.uniform(0.2, 3.0, p))[::-1]
    for scen in range(2):
        if scen == 1: lam = np.array([3.0] + [1.0] * (p - 1)) if p > 2 else lam   # one dominant direction
        G = rng.normal(size=(N, p)) * np.sqrt(lam)[None, :]     # g in the eigenbasis coordinates
        def E_gamma(x):
            V = expm(skew(x, p))                                 # orthonormal basis columns = rotated eigenbasis
            P = (G @ V) ** 2
            P.sort(axis=1)
            return P[:, p - d:].sum(1).mean()
        base = E_gamma(np.zeros(p * (p - 1) // 2))
        best = base; bx = None
        for rep in range(4):
            x0 = rng.normal(0, 0.8, p * (p - 1) // 2)
            r = minimize(lambda x: -E_gamma(x), x0, method='Nelder-Mead', options={'maxiter': 150, 'xatol': 1e-4, 'fatol': 1e-6})
            if -r.fun > best: best, bx = -r.fun, r.x
        print(f"p={p} d={d} lam={np.round(lam,3)}: eigenbasis E Gamma = {base:.6f}; best rotated = {best:.6f}; excess = {best-base:+.6f} (MC se ~ {np.sqrt(lam.sum())/np.sqrt(N):.5f})")
        if bx is not None and best - base > 3 * np.sqrt(lam.sum()) / np.sqrt(N):
            print("   candidate violation, rotation params", np.round(bx, 4))
