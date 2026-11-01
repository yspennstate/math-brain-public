# E0065 / Problem 12: is the vertex-ansatz bound alpha_3 >= 1/12 improvable?
# At a FIXED floor lam, maximise  r(P) = min over fixed points in S^2 of the tangent
# spectral radius, over all QSOs with min entry >= lam.  r > 1 certifies non-regularity.
# Positive control: at lam just below 1/12 the search must find r > 1.
import numpy as np, time, sys
np.seterr(all='ignore')
PR = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
MU = np.array([1., 2., 2., 1., 2., 1.])
I = np.array([p[0] for p in PR]); J = np.array([p[1] for p in PR])
m = 3

def Vmap(P, x):
    return (MU * x[I] * x[J]) @ P

def Jac(P, x):
    M = np.zeros((3, 3))
    for idx, (i, j) in enumerate(PR):
        c = 1.0 if i == j else 2.0
        M[:, j] += c * P[idx] * x[i]
        M[:, i] += c * P[idx] * x[j]
    return M

def rho_t(P, x):
    ev = np.linalg.eigvals(Jac(P, x))
    k = int(np.argmin(np.abs(ev - 2.0)))
    return float(np.max(np.abs(np.delete(ev, k))))

rng0 = np.random.default_rng(17)
SEEDS = [np.eye(3)[k] for k in range(3)] + [np.ones(3) / 3] + \
        [rng0.dirichlet(np.ones(3) * 0.7) for _ in range(45)]

def fixed_points(P):
    pts = []
    Im = np.eye(3)
    for x0 in SEEDS:
        x = x0.astype(float).copy(); ok = False
        for _ in range(45):
            F = Vmap(P, x) - x
            M = Jac(P, x) - Im
            T = M[:2, :2] - M[:2, 2][:, None]
            try:
                du = np.linalg.solve(T, -F[:2])
            except Exception:
                break
            dx = np.concatenate([du, [-du.sum()]])
            x = x + dx
            if not np.all(np.isfinite(x)):
                break
            if np.max(np.abs(dx)) < 1e-13:
                ok = True; break
        if not ok or not np.all(np.isfinite(x)) or x.min() < -1e-9 or abs(x.sum() - 1) > 1e-9:
            continue
        x = np.clip(x, 0.0, None); x = x / x.sum()
        if np.max(np.abs(Vmap(P, x) - x)) < 1e-11 and not any(np.max(np.abs(x - q)) < 1e-7 for q in pts):
            pts.append(x)
    return pts

def score(P):
    fp = fixed_points(P)
    if not fp:
        return -1.0
    return min(rho_t(P, x) for x in fp)

def mk(Q, lam):
    return lam + (1 - 3 * lam) * Q

def vertex_seeds():
    import itertools
    out = []
    for sig in itertools.product(range(3), repeat=6):
        Q = np.zeros((6, 3))
        for idx, k in enumerate(sig):
            Q[idx, k] = 1.0
        out.append(Q)
    return out

VSEEDS = vertex_seeds()

def search(lam, rng, restarts=4000, refine=6000):
    best = -1.0; bQ = None
    for Q in VSEEDS:                      # POSITIVE CONTROL: the vertex ansatz is in the pool
        s = score(mk(Q, lam))
        if s > best:
            best, bQ = s, Q.copy()
    print(f"   [vertex-ansatz best at lam={lam:.4f}: {best:.8f}]", flush=True)
    for _ in range(restarts):
        Q = rng.dirichlet(np.ones(3) * 0.35, size=6)
        s = score(mk(Q, lam))
        if s > best:
            best, bQ = s, Q.copy()
    cur, cs = bQ, best
    for k in range(refine):
        sc = 0.45 * (1 - k / refine) + 0.005
        Q = np.abs(cur + rng.normal(0, sc, size=(6, 3))); Q /= Q.sum(1, keepdims=True)
        s = score(mk(Q, lam))
        if s > cs:
            cs, cur = s, Q.copy()
    return cs, mk(cur, lam)

if __name__ == "__main__":
    rng = np.random.default_rng(2026913)
    t0 = time.time()
    for lam in [0.080, 0.0833, 0.0840, 0.0860, 0.0886, 0.095, 0.11, 0.13, 0.15]:
        s, P = search(lam, rng)
        print(f"lam={lam:.4f}  best min-over-fixed-points spectral radius = {s:.8f}  "
              f"{'NON-REGULAR EXISTS' if s > 1 else 'none found'}   [{time.time()-t0:.0f}s]",
              flush=True)
        if s > 1:
            np.save(f"e0065_m3_gen_{int(lam*10000)}.npy", P)
            print(np.array2string(P, precision=8), flush=True)
