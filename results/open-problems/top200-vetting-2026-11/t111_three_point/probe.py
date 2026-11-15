"""T111 probe: sup over n <= NMAX of sqrt(n) * Delta_n / beta3 for iid three-point laws.

Delta_n = sup_x |P(S_n/sqrt(n) <= x) - Phi(x)| for standardized summands, computed exactly
from the multinomial law of the atom counts (left and right limits at every atom of S_n).
Esseen's constant C_E = (sqrt(10)+3)/(6 sqrt(2 pi)) is the conjectured supremum.
"""
import math
import sys
import numpy as np
from scipy.special import gammaln, ndtr
from scipy.optimize import minimize

CE = (math.sqrt(10) + 3) / (6 * math.sqrt(2 * math.pi))
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 400
rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 1)

# precompute multinomial index grids per n
GRID = {}
for n in range(1, NMAX + 1):
    i, j = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing="ij")
    m = i + j <= n
    i, j = i[m], j[m]
    k = n - i - j
    lc = gammaln(n + 1) - gammaln(i + 1) - gammaln(j + 1) - gammaln(k + 1)
    GRID[n] = (i, j, k, lc)


def law(theta):
    """theta -> standardized three-point law (atoms, probs)."""
    a, b, c = np.sort(theta[:3])
    w = np.exp(theta[3:6] - np.max(theta[3:6]))
    p = w / w.sum()
    x = np.array([a, b, c])
    mu = p @ x
    sd = math.sqrt(max(p @ (x - mu) ** 2, 1e-300))
    x = (x - mu) / sd
    return x, p


def ratio_n(x, p, n):
    i, j, k, lc = GRID[n]
    lp = lc + i * math.log(max(p[0], 1e-300)) + j * math.log(max(p[1], 1e-300)) + k * math.log(max(p[2], 1e-300))
    s = (i * x[0] + j * x[1] + k * x[2]) / math.sqrt(n)
    o = np.argsort(s, kind="stable")
    s, pr = s[o], np.exp(lp[o])
    # merge equal support points
    keep = np.r_[True, np.diff(s) > 1e-12]
    grp = np.cumsum(keep) - 1
    pr = np.bincount(grp, weights=pr)
    s = s[keep]
    F = np.cumsum(pr)
    Fl = F - pr
    ph = ndtr(s)
    return max(np.max(np.abs(F - ph)), np.max(np.abs(Fl - ph)))


def score(theta, nmax=NMAX):
    x, p = law(theta)
    b3 = p @ np.abs(x) ** 3
    best, bn = 0.0, 0
    for n in range(1, nmax + 1):
        r = math.sqrt(n) * ratio_n(x, p, n) / b3
        if r > best:
            best, bn = r, n
    return best, bn, x, p


if __name__ == "__main__":
    # sanity: Esseen's two-point law (third atom of zero mass) should stay below C_E
    p0 = (4 - math.sqrt(10)) / 2
    th = np.array([0.0, 1.0, 1.0 + 1e-9, math.log(1 - p0), math.log(p0) , -60.0])
    r, n, _, _ = score(th)
    print(f"two-point Esseen law: max ratio {r:.6f} at n={n}; C_E={CE:.6f}")
    out = []
    for t in range(TRIALS):
        th = np.r_[rng.normal(size=3) * 2, rng.normal(size=3) * 1.5]
        r, n, x, p = score(th, nmax=min(NMAX, 25))
        out.append((r, th))
    out.sort(key=lambda z: -z[0])
    print("best random (n<=25):", [round(z[0], 5) for z in out[:5]])
    for r0, th in out[:4]:
        res = minimize(lambda t: -score(t, nmax=min(NMAX, 25))[0], th, method="Nelder-Mead",
                       options={"maxiter": 600, "xatol": 1e-7, "fatol": 1e-9})
        r, n, x, p = score(res.x)
        print(f"local max: ratio {r:.6f} at n={n} (C_E-ratio {CE - r:+.6f}) atoms {np.round(x, 4)} probs {np.round(p, 4)}")
