# Exact partition functions for the balls-in-boxes model B_{m,n} with weights w,
# and the two-scale tilt criterion for the appearance of a box of size b.
# Z(m,n) = sum over (y_1..y_n), sum y_i = m, of prod w_{y_i}.  Computed in log space.
import numpy as np, math, itertools, sys
from scipy.optimize import brentq

def logZ_table(logw, supp, n_max, m_max):
    """logZ[n][m] for 0<=n<=n_max, 0<=m<=m_max. logw: dict k->log w_k on supp."""
    NEG = -np.inf
    Z = np.full((n_max+1, m_max+1), NEG)
    Z[0,0] = 0.0
    for n in range(1, n_max+1):
        row = np.full(m_max+1, NEG)
        for k in supp:
            if k > m_max: continue
            shifted = np.full(m_max+1, NEG)
            shifted[k:] = Z[n-1, :m_max+1-k] + logw[k]
            row = np.logaddexp(row, shifted)
        Z[n] = row
    return Z

def brute_Z(w, supp, m, n):
    tot = 0.0
    for ys in itertools.product(supp, repeat=n):
        if sum(ys) == m:
            p = 1.0
            for y in ys: p *= w[y]
            tot += p
    return tot

def tilt_root(w, supp, cut, lam):
    """t>0 with Psi_<(t)=lam for the weights truncated to supp∩[0,cut)."""
    ks = np.array([k for k in supp if k < cut], dtype=float)
    ws = np.array([w[k] for k in supp if k < cut])
    def G(logt):
        z = np.log(ws) + ks*logt
        e = np.exp(z - z.max())  # rescaled by the largest term, sign-safe
        return float(np.sum((ks - lam)*e))
    lo, hi = -5.0, 0.0
    while G(hi) < 0: hi += 0.5
    while G(lo) > 0: lo -= 1.0
    return math.exp(brentq(G, lo, hi, xtol=1e-14))

def logPhi(w, supp, cut, t):
    return math.log(sum(w[k]*t**k for k in supp if k < cut))

if __name__ == "__main__":
    # sanity: DP vs brute force on a tiny irregular example
    supp = [0,1,2,5]
    w = {0:1.0, 1:0.7, 2:0.05, 5:0.3}
    logw = {k: math.log(w[k]) for k in supp}
    Z = logZ_table(logw, supp, 6, 12)
    ok = True
    for n in range(1,7):
        for m in range(0,13):
            b = brute_Z(w, supp, m, n)
            d = math.exp(Z[n,m]) if Z[n,m] > -np.inf else 0.0
            if abs(b-d) > 1e-12*max(1,b): ok = False; print("MISMATCH", n, m, b, d)
    print("DP vs brute force on 6x13 grid:", "OK" if ok else "FAIL")
