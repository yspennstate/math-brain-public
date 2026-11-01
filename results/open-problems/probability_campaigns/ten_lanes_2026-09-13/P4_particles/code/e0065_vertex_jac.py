# alpha_m by the "vertex ansatz" P_{ij,.} = lam*1 + (1-m*lam) e_{sigma(ij)},
# with the RIGOROUS certificate: every fixed point of V in the simplex has tangent
# spectral radius > 1  =>  no trajectory converges  =>  V is not regular.
# m=2 is a positive control: the answer must be (3-sqrt7)/4 = 0.0885621722...
import numpy as np, itertools, math, sys, time
np.seterr(all='ignore')

def setup(m):
    PR = [(i, j) for i in range(m) for j in range(i, m)]
    MU = np.array([1.0 if i == j else 2.0 for i, j in PR])
    I = np.array([p[0] for p in PR]); J = np.array([p[1] for p in PR])
    return PR, MU, I, J

def Vmap(P, MU, I, J, x):
    return (MU * x[I] * x[J]) @ P

def Jac(P, PR, x, m):
    M = np.zeros((m, m))
    for idx, (i, j) in enumerate(PR):
        M[:, j] += P[idx] * x[i]
        M[:, i] += P[idx] * x[j]
    return M

def tangent_rho(P, PR, x, m):
    M = Jac(P, PR, x, m)
    ev = np.linalg.eigvals(M)
    k = int(np.argmin(np.abs(ev - 2.0)))          # columns of M sum to 2
    ev = np.delete(ev, k)
    return float(np.max(np.abs(ev)))

def fixed_points(P, PR, MU, I, J, m, grid_seeds):
    pts = []
    for x0 in grid_seeds:
        x = x0.astype(float).copy()
        ok = False
        for _ in range(120):
            F = Vmap(P, MU, I, J, x) - x
            A = np.vstack([Jac(P, PR, x, m) - np.eye(m), np.ones(m)])
            b = np.concatenate([-F, [0.0]])
            try:
                dx, *_ = np.linalg.lstsq(A, b, rcond=None)
            except Exception:
                break
            x = x + dx
            if not np.all(np.isfinite(x)):
                break
            if np.max(np.abs(dx)) < 1e-14:
                ok = True
                break
        if not ok or not np.all(np.isfinite(x)):
            continue
        if x.min() < -1e-9 or abs(x.sum() - 1) > 1e-8:
            continue
        x = np.clip(x, 0.0, None); x = x / x.sum()
        if np.max(np.abs(Vmap(P, MU, I, J, x) - x)) < 1e-11:
            if not any(np.max(np.abs(x - q)) < 1e-7 for q in pts):
                pts.append(x)
    return pts

def seeds(m, n=9):
    out = [np.eye(m)[k] for k in range(m)] + [np.ones(m) / m]
    rng = np.random.default_rng(17)
    for _ in range(120):
        out.append(rng.dirichlet(np.ones(m) * 0.6))
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

def best_lam(m, PR, MU, I, J, sig, sd):
    lo, hi = 0.0, 1.0 / m
    ok0, _, _ = certified_nonregular(build(m, PR, sig, 0.0), PR, MU, I, J, m, sd)
    if not ok0:
        return 0.0, None
    for _ in range(44):
        mid = (lo + hi) / 2
        ok, r, nf = certified_nonregular(build(m, PR, sig, mid), PR, MU, I, J, m, sd)
        if ok:
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
        best = (-1.0, None, None)
        t0 = time.time()
        for sig in itertools.product(range(m), repeat=len(PR)):
            L, P = best_lam(m, PR, MU, I, J, sig, sd)
            if L > best[0]:
                best = (L, sig, P)
                print(f"  m={m} sigma={sig} lam={L:.12f}  [{time.time()-t0:.0f}s]", flush=True)
        print(f"m={m}: VERTEX-ANSATZ MAX lam = {best[0]:.12f}  sigma={best[1]}", flush=True)
        if m == 2:
            print("   control target (3-sqrt7)/4 =", (3 - math.sqrt(7)) / 4, flush=True)
        if best[2] is not None:
            np.save(f"e0065_vertexjac_best_m{m}.npy", best[2])
            print(np.array2string(best[2], precision=10), flush=True)
