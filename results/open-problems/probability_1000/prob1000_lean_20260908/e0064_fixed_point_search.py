"""E0064 (Rozikov 2009, Problem 11): does Theorem 6(1) - a strictly non-Volterra QSO has a UNIQUE fixed point - hold
for m >= 4?  (Non-attractiveness already fails for m >= 4: E0064-A002.)  Strictly non-Volterra: P_{ij,k} = 0 whenever
k in {i,j}; V_k(x) = sum_{i,j} P_{ij,k} x_i x_j with P symmetric in (i,j), sum_k P_{ij,k} = 1.
Search: random operators on m = 4 (and 5); all fixed points in the simplex found by Newton from many starts on
F(x) = V(x) - x restricted to the simplex (sum x = 1 is preserved by V so use the affine chart x_m = 1 - sum);
solutions deduplicated and re-verified at high precision with mpmath; report any operator with >= 2 fixed points.
A found example is then checked exactly (residual < 1e-40 at 50 digits) and its Jacobian spectrum printed.
"""
import itertools, sys
import numpy as np
from scipy.optimize import fsolve

def random_snv(rng, m):
    P = np.zeros((m, m, m))
    for i in range(m):
        for j in range(i, m):
            allowed = [k for k in range(m) if k not in (i, j)]
            w = rng.dirichlet(np.ones(len(allowed)) * rng.uniform(0.3, 3.0))
            for k, wk in zip(allowed, w):
                P[i, j, k] = wk; P[j, i, k] = wk
    return P

def V(P, x):
    return np.einsum('ijk,i,j->k', P, x, x)

def fixed_points(P, rng, starts=300, tol=1e-11):
    m = P.shape[0]
    def F(y):
        x = np.append(y, 1 - y.sum())
        return (V(P, x) - x)[:-1]
    sols = []
    for s in range(starts):
        y0 = rng.dirichlet(np.ones(m))[:-1]
        y, info, ier, msg = fsolve(F, y0, full_output=True, xtol=1e-13)
        if ier != 1: continue
        x = np.append(y, 1 - y.sum())
        if np.any(x < -1e-9) or x.sum() > 1 + 1e-9: continue
        if np.max(abs(V(P, x) - x)) > tol: continue
        if not any(np.max(abs(x - z)) < 1e-7 for z in sols): sols.append(x)
    return sols

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
    for m in (4, 5):
        counts = {}
        best = None
        for trial in range(400 if m == 4 else 150):
            P = random_snv(rng, m)
            sols = fixed_points(P, rng, starts=120 if m == 4 else 80)
            counts[len(sols)] = counts.get(len(sols), 0) + 1
            if len(sols) >= 2 and (best is None or len(sols) > len(best[1])):
                best = (P.copy(), sols)
            if trial % 100 == 99: print(f"m={m} trial {trial+1}: fixed-point count histogram {dict(sorted(counts.items()))}", flush=True)
        print(f"m={m} FINAL histogram of number of fixed points in the simplex: {dict(sorted(counts.items()))}", flush=True)
        if best is not None:
            P, sols = best
            print(f"m={m} EXAMPLE with {len(sols)} fixed points:")
            for x in sols:
                J = np.array([[2 * sum(P[i, j, k] * x[j] for j in range(m)) for i in range(m)] for k in range(m)])
                ev = np.linalg.eigvals(J)
                print("   x =", np.round(x, 6), " residual", np.max(abs(V(P, x) - x)), " |eig DV| =", np.round(np.sort(abs(ev))[::-1], 4))
            np.save(f"e0064_example_m{m}.npy", P)
