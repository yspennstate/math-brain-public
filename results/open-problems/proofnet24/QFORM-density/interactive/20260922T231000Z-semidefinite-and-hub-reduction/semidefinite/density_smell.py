try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Smell test for Theorem 1: histogram peak densities of PSD forms with lambda_3 >= 1 (normalized to lambda_3 = 1)
# in the configurations newly covered: heavy coordinate + linear term outside the range; huge eigenvalue; spread laws.
import numpy as np
rng = np.random.default_rng(31)

def sample_laws(n, N, kind):
    if kind == "uniform":
        return rng.uniform(-0.5, 0.5, size=(N, n))
    # spread: uniform on m intervals of length 1/m placed at random over [-L, L]
    m = 5; L = 20.0
    starts = rng.uniform(-L, L, size=(n, m))
    which = rng.integers(0, m, size=(N, n))
    off = rng.uniform(0, 1.0 / m, size=(N, n))
    return starts[np.arange(n)[None, :], which] + off

def peak(Q, width=0.004):
    lo, hi = np.quantile(Q, [0.0005, 0.9995])
    bins = np.arange(lo, hi + width, width)
    h, _ = np.histogram(Q, bins=bins)
    return h.max() / (len(Q) * width)

def frame(n, r):
    Qm, _ = np.linalg.qr(rng.standard_normal((n, r)))
    return Qm

N = 1_500_000
CH = 150_000
def qvals(n, kind, A, lin):
    parts = []
    for _ in range(N // CH):
        X = sample_laws(n, CH, kind)
        parts.append(np.einsum("ij,jk,ik->i", X, A, X) + X @ lin)
    return np.concatenate(parts)
out = []
for n in (12, 60):
    for kind in ("uniform", "spread"):
        # (E1) rank-3 projection with one heavy coordinate (leverage ~ 0.6) + linear term outside the range
        R = frame(n, 3)
        e0 = np.zeros(n); e0[0] = 1.0
        R[:, 0] = 0.77 * e0 + 0.64 * R[:, 0] * (1 - e0)
        R, _ = np.linalg.qr(R)
        A = R @ R.T
        z = rng.standard_normal(n); z -= R @ (R.T @ z); z /= np.linalg.norm(z)
        for beta in (0.0, 0.5, 2.0):
            Q = qvals(n, kind, A, beta * z)
            out.append((f"E1 rank3 proj heavy lev {A[0,0]:.2f} beta={beta}", n, kind, peak(Q)))
        # (E2) huge eigenvalue + two at 1, random linear term
        R = frame(n, 3)
        A = (R * np.array([50.0, 1.0, 1.0])) @ R.T
        b = rng.standard_normal(n)
        Q = qvals(n, kind, A, b)
        out.append(("E2 (50,1,1) + random b", n, kind, peak(Q)))
        # (E3) X_1^2 + two spread squares + term outside range
        R = frame(n - 1, 2)
        A = np.zeros((n, n)); A[0, 0] = 1.0; A[1:, 1:] = R @ R.T
        z = np.zeros(n); zz = rng.standard_normal(n - 1); zz -= R @ (R.T @ zz); z[1:] = zz / np.linalg.norm(zz)
        Q = qvals(n, kind, A, 1.0 * z)
        out.append(("E3 X1^2 + spread rank2 + z-term", n, kind, peak(Q)))
        for row in out[-5:]:
            print(f"{row[0]:40s} n={row[1]:3d} {row[2]:8s} peak density ~ {row[3]:.3f}", flush=True)
print("max over all:", max(r[3] for r in out), "(Theorem 1 bound 1.71e4; Gaussian benchmark 3 sqrt 2 = 4.24 for (1,1,-1))", flush=True)
