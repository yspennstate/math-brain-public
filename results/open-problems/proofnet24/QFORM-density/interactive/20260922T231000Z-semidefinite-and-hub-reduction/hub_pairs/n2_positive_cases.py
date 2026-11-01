"""N2. Sup over s of the density of Q for two hubs, several hub blocks and remainders.
Exact conditional sublevel estimator (given X' and X_{h1}), P(|Q - s| <= eps)/(2 eps) on an s-grid,
coarse eps then a refinement around the maximum.  Cases:
  A  : Theorem A (pure leaves, remainder zero on the leaves), indefinite and definite hub blocks, spread hub laws.
  B  : Theorem B, B = diag(a, 0) with the adversarial remainder R = L1^2/a (Schur matching in the first hub).
  D  : definite B = b I with R = t L^T B^{-1} L, t in {0, .5, 1, 1.5, 2}, b in {0.2, 0.05, 0.01}  (open case).
  I3 : indefinite B with R = t L^T B^{-1} L, t near 1, and with a third direction added (open case).
"""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import sys, time
import numpy as np
sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('/', 1)[0])
from hubpair_lib import UnionLaw, pair_prob, spread_rows

rng = np.random.default_rng(7)
m, sigma = 60, 1.0
A = spread_rows(m, sigma, rng)
v3 = rng.standard_normal(m); v3 -= A.T @ np.linalg.lstsq(A.T, v3, rcond=None)[0]; v3 /= np.linalg.norm(v3)
N = 150_000
t0 = time.time()
Xp = rng.random((N, m)) - 0.5
L = Xp @ A.T
V3 = Xp @ v3
law_int = UnionLaw.interval()
law_spr1 = UnionLaw.spread(5, 8.0, rng)
law_spr2 = UnionLaw.spread(7, 12.0, rng)


def sup_density(B, r, law1, law2, s_grid, eps_c=4e-3, eps_f=4e-4, reuse_x1=None):
    B = np.array(B, float)
    c = 2 * L
    x1 = law1.sample(N, rng) if reuse_x1 is None else reuse_x1
    vals = np.array([pair_prob(B, c[:, 0], c[:, 1], r, x1, s, eps_c, law2).mean() / (2 * eps_c) for s in s_grid])
    k = int(np.argmax(vals))
    s0 = s_grid[k]
    ds = (s_grid[1] - s_grid[0])
    fine = np.linspace(s0 - ds, s0 + ds, 21)
    fv = np.array([pair_prob(B, c[:, 0], c[:, 1], r, x1, s, eps_f, law2).mean() / (2 * eps_f) for s in fine])
    kf = int(np.argmax(fv))
    return vals[k], s0, fv[kf], fine[kf]


def report(label, B, r, laws=(law_int, law_int), grid=np.linspace(-4, 4, 161)):
    coarse, s0, fine, s1 = sup_density(B, r, laws[0], laws[1], grid)
    print(f"{label:62s} sup(coarse eps) {coarse:6.3f} at s={s0:+.3f}; refined {fine:6.3f} at s={s1:+.4f}  [{time.time()-t0:.0f}s]", flush=True)
    return fine


print("Theorem A bound sqrt(2 pi)/sigma =", np.sqrt(2*np.pi)/sigma, flush=True)
zero = np.zeros(N)
Wk = 1.3 * (rng.random(N) - 0.5) ** 2 * 3  # an independent K-part (e.g. 3.9 X_k^2), makes the rest nontrivial
for lawsname, laws in [("uniform hubs", (law_int, law_int)), ("spread hubs", (law_spr1, law_spr2))]:
    report(f"A  indefinite B=diag(.3,-.3), R=0 on leaves, {lawsname}", [[.3, 0], [0, -.3]], zero, laws)
    report(f"A  B=[[.1,.25],[.25,-.2]], R=W(X_K), {lawsname}", [[.1, .25], [.25, -.2]], Wk, laws)
    report(f"A  definite B=diag(.3,.3), R=0, {lawsname}", [[.3, 0], [0, .3]], zero, laws)

print("Theorem B bound 1 + 9.52/(s2 s1^0.5) =", 1 + 9.52, flush=True)
for a in [1.0, 0.2, 0.02]:
    for lawsname, laws in [("uniform", (law_int, law_int)), ("spread", (law_spr1, law_spr2))]:
        report(f"B  B=diag({a},0), R=L1^2/a (Schur match in hub 1), {lawsname}", [[a, 0], [0, 0]], L[:, 0] ** 2 / a, laws)

for b in [0.2, 0.05, 0.01]:
    Binv = np.eye(2) / b
    for t in [0.0, 0.5, 1.0, 1.5, 2.0]:
        r = t * np.einsum('ni,ij,nj->n', L, Binv, L)
        grid = np.linspace(-4, 4, 161) if t <= 1 else np.linspace(-4, 4 + 30 * (t - 1) / b * 0.1, 161)
        report(f"D  definite B={b}I, R={t} L^T B^-1 L, spread hubs", [[b, 0], [0, b]], r, (law_spr1, law_spr2), grid)
print("done", flush=True)
