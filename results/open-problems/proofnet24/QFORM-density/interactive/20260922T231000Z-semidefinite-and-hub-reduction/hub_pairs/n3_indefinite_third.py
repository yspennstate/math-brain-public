"""N3. Indefinite hub block near Schur matching, and the effect of a third large direction.
B = diag(b, -b).  R = t L^T B^{-1} L  (t = 1: exact matching, rank-two form, log-divergent density at 0).
Then R = L^T B^{-1} L + lam V3^2 with V3 = <v3, X'>, v3 orthogonal to the hub rows (a third eigenvalue carried by the
leaves themselves, so xi = lam V3^2 is dependent on Z but not a function of it).
Also R = L^T B^{-1} L + 4 X_k^2 with an extra independent coordinate (the independent-third-structure model).
Estimator: exact conditional sublevel probability; for each case the ratio P(|Q - s|<=eps)/(2 eps) at eps = 1e-2..1e-6,
at the worst s found on a coarse grid."""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import sys, time
import numpy as np
sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('/', 1)[0])
from hubpair_lib import UnionLaw, pair_prob, spread_rows

rng = np.random.default_rng(11)
m, sigma = 60, 1.0
A = spread_rows(m, sigma, rng)
v3 = rng.standard_normal(m); v3 -= A.T @ np.linalg.lstsq(A.T, v3, rcond=None)[0]; v3 /= np.linalg.norm(v3)
N = 120_000
Xp = rng.random((N, m)) - 0.5
L = Xp @ A.T
V3 = Xp @ v3
Xk = rng.random(N) - 0.5
law = UnionLaw.interval()
x1 = law.sample(N, rng)
t0 = time.time()
b = 0.2
B = np.array([[b, 0], [0, -b]])
Binv = np.linalg.inv(B)
S = np.einsum('ni,ij,nj->n', L, Binv, L)
c = 2 * L


def dens(r, s, eps):
    return pair_prob(B, c[:, 0], c[:, 1], r, x1, s, eps, law).mean() / (2 * eps)


def profile(label, r, grid=np.linspace(-1.5, 1.5, 61)):
    vals = np.array([dens(r, s, 3e-3) for s in grid])
    s0 = grid[int(np.argmax(vals))]
    row = [dens(r, s0, e) for e in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]]
    print(f"{label:48s} worst s={s0:+.3f}: " + "  ".join(f"{v:6.3f}" for v in row) + f"   [{time.time()-t0:.0f}s]", flush=True)


print("columns: P(|Q-s|<=eps)/(2eps) at eps = 1e-2, 1e-3, 1e-4, 1e-5, 1e-6", flush=True)
for t in [1.0, 0.99, 0.9, 0.5, 0.0]:
    profile(f"R = {t} L^T B^-1 L", t * S)
for lam in [0.25, 1.0, 4.0]:
    profile(f"R = L^T B^-1 L + {lam} V3^2 (third dir. in leaves)", S + lam * V3 ** 2)
profile("R = L^T B^-1 L + 4 X_k^2 (independent coordinate)", S + 4 * Xk ** 2)
profile("R = L^T B^-1 L + 4 X_k^2 - 4 X_k'^2 (two indep.)", S + 4 * Xk ** 2 - 4 * (rng.random(N) - 0.5) ** 2)
print("done", flush=True)
