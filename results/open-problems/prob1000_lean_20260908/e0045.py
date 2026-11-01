"""E0045 (Bandeira Open Problem 1.1, Mallat-Zeitouni): g ~ N(0,Sigma) in R^p; for an orthonormal basis V,
Gamma_V = max_{|S|=d} sum_{i in S} (v_i . g)^2.  Conjecture: the eigenbasis of Sigma maximises E Gamma_V.
Search: common random numbers, p in {3,4}, d in {2,3}; compare the eigenbasis against many rotations and a local optimiser."""
import numpy as np
from scipy.optimize import minimize
from scipy.stats import special_ortho_group
rng = np.random.default_rng(45)
def EGamma(V, Z, sig, d):
    # g = diag(sig) z ; projections onto columns of V
    proj = (Z*sig) @ V            # N x p
    sq = proj**2
    top = np.sort(sq, axis=1)[:, -d:]
    return top.sum(1).mean()
N = 200_000
worst = []
for p, d in [(3,2),(4,2),(4,3),(5,2),(5,3)]:
    Z = rng.standard_normal((N, p))
    best_gain = -1; rec = None
    for trial in range(12):
        sig = np.sort(rng.uniform(0.2, 1.0, p))[::-1] if trial % 2 == 0 else np.array([1.0]*(p-1) + [rng.uniform(0.05,0.9)])
        if trial == 1: sig = np.array([1.0, 1.0, 0.3] + [0.3]*(p-3))
        base = EGamma(np.eye(p), Z, sig, d)
        # random rotations
        bestR = base; bestV = np.eye(p)
        for _ in range(40):
            V = special_ortho_group.rvs(p, random_state=rng)
            val = EGamma(V, Z, sig, d)
            if val > bestR: bestR, bestV = val, V
        # local optimisation over so(p) via Cayley-like parametrisation from the best rotation
        from scipy.linalg import expm
        k = p*(p-1)//2
        def V_of(x):
            A = np.zeros((p,p)); idx = np.triu_indices(p,1); A[idx] = x; A = A - A.T
            return bestV @ expm(A)
        res = minimize(lambda x: -EGamma(V_of(x), Z, sig, d), np.zeros(k), method='Nelder-Mead', options={'maxfev':200,'xatol':1e-4})
        opt = -res.fun
        gain = (max(bestR, opt) - base)/base
        if gain > best_gain: best_gain = gain; rec = (sig.round(3).tolist(), base, max(bestR,opt))
    se = 1.0/np.sqrt(N)   # rough relative scale of the MC noise (common random numbers make the comparison much tighter)
    print(f"p={p} d={d}: largest relative gain over the eigenbasis found = {best_gain:+.5f}   (sig, E_eigen, E_best) = {rec}")
