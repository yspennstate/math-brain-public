# alpha_m by the "vertex ansatz" P_{ij,.} = lam*1 + (1-m*lam) e_{sigma(ij)}.
# Certificate: EVERY fixed point of V in S^{m-1} has tangent spectral radius > 1
#   => no trajectory converges => V is not regular.  (Sufficient, not necessary,
#      so the number produced is a LOWER bound for alpha_m.)
# m=2 is a positive control: the answer must be (3-sqrt7)/4 = 0.08856217223385232.
#
# v2 fixes the Jacobian: the off-diagonal pair (i,j), i<j, carries the factor 2.
import numpy as np, itertools, math, time, sys
np.seterr(all='ignore')

def setup(m):
    PR = [(i, j) for i in range(m) for j in range(i, m)]
    MU = np.array([1.0 if i == j else 2.0 for i, j in PR])
    I = np.array([p[0] for p in PR]); J = np.array([p[1] for p in PR])
    return PR, MU, I, J

def Vmap(P, MU, I, J, x):
    return (MU * x[I] * x[J]) @ P

def Jac(P, PR, x, m):
    """dV_k/dx_l ; columns sum to 2 at any x with sum x = 1."""
    M = np.zeros((m, m))
    for idx, (i, j) in enumerate(PR):
        c = 1.0 if i == j else 2.0
        M[:, j] += c * P[idx] * x[i]
        M[:, i] += c * P[idx] * x[j]
    return M

def tangent_rho(P, PR, x, m):
    M = Jac(P, PR, x, m)
    ev = np.linalg.eigvals(M)
    k = int(np.argmin(np.abs(ev - 2.0)))
    return float(np.max(np.abs(np.delete(ev, k))))

def fixed_points(P, PR, MU, I, J, m, sd):
    """Newton in the reduced coordinates u = x_1..x_{m-1}, x_m = 1 - sum u."""
    pts = []
    Im = np.eye(m)
    for x0 in sd:
        x = x0.astype(float).copy()
        ok = False
        for _ in range(40):
            F = Vmap(P, MU, I, J, x) - x
            M = Jac(P, PR, x, m) - Im
            # restrict to the tangent space: du free in R^{m-1}, dx_m = -sum du
            T = M[:m - 1, :m - 1] - M[:m - 1, m - 1][:, None]
            try:
                du = np.linalg.solve(T, -F[:m - 1])
            except Exception:
                break
            dx = np.concatenate([du, [-du.sum()]])
            x = x + dx
            if not np.all(np.isfinite(x)):
                break
            if np.max(np.abs(dx)) < 1e-13:
                ok = True
                break
        if not ok or not np.all(np.isfinite(x)):
            continue
        if x.min() < -1e-9 or abs(x.sum() - 1) > 1e-9:
            continue
        x = np.clip(x, 0.0, None); x = x / x.sum()
        if np.max(np.abs(Vmap(P, MU, I, J, x) - x)) < 1e-11:
            if not any(np.max(np.abs(x - q)) < 1e-7 for q in pts):
                pts.append(x)
    return pts

def seeds(m, n=40):
    out = [np.eye(m)[k] for k in range(m)] + [np.ones(m) / m]
    rng = np.random.default_rng(17)
    for _ in range(n):
        out.append(rng.dirichlet(np.ones(m) * 0.7))
    return out

def build(m, PR, sig, lam):
    P = np.full((len(PR), m), lam)
    for idx, k in enumerate(sig):
        P[idx, k] += 1 - m * lam
    return P

def certified_nonregular(P, PR, MU, I, J, m, sd):
    fps = fixed_points(P, PR, MU, I, J, m, sd)
    if not fps:
        return False, 0.0, 0
    r = min(tangent_rho(P, PR, x, m) for x in fps)
    return r > 1.0, r, len(fps)

def best_lam(m, PR, MU, I, J, sig, sd, steps=40):
    lo, hi = 0.0, 1.0 / m
    if not certified_nonregular(build(m, PR, sig, 0.0), PR, MU, I, J, m, sd)[0]:
        return 0.0, None
    for _ in range(steps):
        mid = (lo + hi) / 2
        if certified_nonregular(build(m, PR, sig, mid), PR, MU, I, J, m, sd)[0]:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-13:
            break
    return lo, build(m, PR, sig, lo)

if __name__ == "__main__":
    for m in (2, 3):
        PR, MU, I, J = setup(m)
        sd = seeds(m)
        best = (-1.0, None, None); t0 = time.time(); allres = []
        for sig in itertools.product(range(m), repeat=len(PR)):
            L, P = best_lam(m, PR, MU, I, J, sig, sd)
            allres.append((L, sig))
            if L > best[0]:
                best = (L, sig, P)
                print(f"  m={m} sigma={sig} lam={L:.12f}  [{time.time()-t0:.0f}s]", flush=True)
        print(f"m={m}: VERTEX-ANSATZ MAX lam = {best[0]:.12f}  sigma={best[1]}  "
              f"[{time.time()-t0:.0f}s]", flush=True)
        if m == 2:
            tgt = (3 - math.sqrt(7)) / 4
            print(f"   CONTROL target (3-sqrt7)/4 = {tgt:.12f}   "
                  f"{'PASS' if abs(best[0]-tgt)<1e-8 else 'FAIL'}", flush=True)
        allres.sort(reverse=True)
        print("   top 8:", [(round(L, 10), s) for L, s in allres[:8]], flush=True)
        if best[2] is not None:
            np.save(f"e0065_vertexjac2_best_m{m}.npy", best[2])
            print(np.array2string(best[2], precision=10), flush=True)
