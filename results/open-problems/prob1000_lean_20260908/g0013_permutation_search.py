"""G0013 (Catalano-Lavenant conjecture) discrete test, 2026-09-10, claude-prob1000-0910.

Continuous conjecture: among couplings pi of two uniform[0,1] marginals, the diagonal and antidiagonal
couplings maximise W_2^2(pi, lambda (x) lambda). Discretise: marginals uniform on {(k+1/2)/n}, couplings =
doubly stochastic matrices / n. Since W_2^2(., nu) is convex, the maximum over the Birkhoff polytope is
attained at a permutation matrix, so the discrete conjecture reads: over all permutations sigma of n points,
W_2^2(pi_sigma, U_n (x) U_n) is maximised by the identity and the reversal. Each W_2^2 is a transportation LP
(n^2 grid points of mass 1/n^2 to n atoms of capacity 1/n). Exhaustive for n <= 8.
"""
import itertools, sys, time
import numpy as np
from scipy.optimize import linprog

def w2sq_perm(n, sigma, cost_cache={}):
    pts = (np.arange(n) + 0.5) / n
    gx, gy = np.meshgrid(pts, pts, indexing="ij")
    grid = np.stack([gx.ravel(), gy.ravel()], 1)                 # n^2 sources, mass 1/n^2
    atoms = np.stack([pts, pts[list(sigma)]], 1)                  # n targets, capacity 1/n
    C = ((grid[:, None, :] - atoms[None, :, :]) ** 2).sum(-1)     # n^2 x n
    m = n * n
    # variables x[s, t] >= 0; sum_t x[s,t] = 1/m ; sum_s x[s,t] = 1/n
    A_eq = np.zeros((m + n, m * n)); b_eq = np.zeros(m + n)
    for s in range(m):
        A_eq[s, s * n:(s + 1) * n] = 1; b_eq[s] = 1 / m
    for t in range(n):
        A_eq[m + t, t::n] = 1; b_eq[m + t] = 1 / n
    res = linprog(C.ravel(), A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method="highs")
    assert res.status == 0, res.message
    return res.fun

def main(n):
    t0 = time.time()
    vals = {}
    for sigma in itertools.permutations(range(n)):
        vals[sigma] = w2sq_perm(n, sigma)
    best = max(vals.values())
    arg = [s for s, v in vals.items() if v > best - 1e-9]
    ident = tuple(range(n)); rev = tuple(range(n - 1, -1, -1))
    print(f"n={n}: {len(vals)} permutations, max W2^2={best:.6f} attained by {len(arg)} permutations: "
          f"{arg[:6]}; identity={vals[ident]:.6f} reversal={vals[rev]:.6f}; "
          f"conjecture holds={set(arg) <= {ident, rev}}  ({time.time()-t0:.0f}s)", flush=True)
    # runner-up, to see the gap
    second = max(v for s, v in vals.items() if s not in (ident, rev))
    s2 = [s for s, v in vals.items() if abs(v - second) < 1e-9][:3]
    print(f"      runner-up {second:.6f} at {s2}", flush=True)

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    for n in [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7]:
        main(n)
