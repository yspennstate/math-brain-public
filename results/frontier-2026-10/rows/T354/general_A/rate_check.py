"""T354 Theorem 3 (agent A, 21 Oct 2026): an empirical falsification test of the rate, on the d = 2 nonconvex sum of
drift_bound_check.py (same a, b, c for the same seed). R independent reshuffling streams run side by side (PyTorch Adam, bias
correction on, eta_k = eta0/sqrt(k)); at log-spaced checkpoints k we record E||grad f(x_k)||_phi(x_k) over the R streams,
||u||_phi^2 = sum_j phi_j u_j^2, phi_j = 1/(sqrt(B2_j(x)) + eps), B2_j(x) = mean_i g_ij(x)^2. Theorem 3 says
    min_{k <= T} E||grad f(x_k)||_phi <= rho_* + O(T^(-1/4) polylog T).
Checkpoints only see some k, so the printed running min is an upper bound on the theorem's min; the test fails if, past the
transient, (running min - plateau) decays slower than T^(-1/4), or if the plateau does not scale like 1 - b2 between runs.
The plateau is the mean of E||grad f||_phi over the last eighth of the run's checkpoints. argv: b1 b2 eps n seed R log2T"""
import sys, math
import numpy as np
b1, b2, eps = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
n, seed, R, L = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
rng = np.random.default_rng(seed)
a = rng.uniform(0.5, 1.5, n); c = rng.uniform(1.5, 2.5, n)
b = rng.exponential(1.0, (n, 2)) - 1.0; b -= b.mean(0)
def phinorm(X):                                                     # X (R, 2) -> ||grad f||_phi per stream
    G = a[None, :, None] * X[:, None, :] + b[None] - c[None, :, None] * np.sin(X)[:, None, :]   # (R, n, 2)
    df = G.mean(1); B2 = (G * G).mean(1)
    return np.sqrt((df * df / (np.sqrt(B2) + eps)).sum(1))
print(__doc__, flush=True)
print(f"b1 {b1} b2 {b2} eps {eps} n {n} seed {seed} R {R} T 2^{L}; mean a {a.mean():.3f} mean c {c.mean():.3f}", flush=True)
T = 2 ** L; eta0 = 0.05
cks = sorted(set(int(round(2 ** (q / 4))) for q in range(4 * 6, 4 * L + 1)))
X = np.tile(np.array([2.0, -1.5]), (R, 1)); M = np.zeros((R, 2)); V = np.zeros((R, 2))
ra = np.random.default_rng([seed, 5]); rows = np.arange(R)
perm = np.argsort(ra.random((R, n)), 1); k = 0; ci = 0; runmin = np.inf; out = []
while k < T:
    for t in range(n):
        k += 1
        i = perm[:, t]
        g = a[i, None] * X + b[i] - c[i, None] * np.sin(X)
        M = b1 * M + (1 - b1) * g; V = b2 * V + (1 - b2) * g * g
        X = X - eta0 / math.sqrt(k) * (M / (1 - b1 ** k)) / (np.sqrt(V / (1 - b2 ** k)) + eps)
        if ci < len(cks) and k == cks[ci]:
            e = phinorm(X); E = e.mean(); runmin = min(runmin, E); out.append((k, E, runmin, e.std(ddof=1) / math.sqrt(R)))
            if ci % 4 == 0 or k == T:
                print(f"k {k:>9d}  E|grad f|_phi {E:.4e} (se {out[-1][3]:.1e})  running min {runmin:.4e}", flush=True)
            ci += 1
        if k >= T: break
    perm = np.argsort(ra.random((R, n)), 1)
O = np.array(out); tail = O[-max(4, len(O) // 8):]
plateau = tail[:, 1].mean()
print(f"plateau (last {len(tail)} checkpoints) {plateau:.4e} +- {tail[:, 1].std(ddof=1):.1e}; plateau/(1 - b2) {plateau / (1 - b2):.4f}",
      flush=True)
# slope of log(running min - plateau) against log k, on the checkpoints where the gap is over 3x the plateau's spread
gap = O[:, 2] - plateau; ok = gap > 3 * max(tail[:, 1].std(ddof=1), 1e-12)
if ok.sum() >= 4:
    sl = np.polyfit(np.log(O[ok, 0]), np.log(gap[ok]), 1)[0]
    print(f"gap fit over k {int(O[ok, 0].min())}..{int(O[ok, 0].max())} ({ok.sum()} pts): (running min - plateau) ~ k^{sl:.3f}"
          f"  (Theorem 3 needs <= -0.25 up to logs)", flush=True)
for q in (2 ** 12, 2 ** 15, 2 ** 18, 2 ** L):
    j = np.searchsorted(O[:, 0], q)
    if j < len(O): print(f"  T {int(O[j, 0])}: running min - plateau {O[j, 2] - plateau:+.3e}   x T^(1/4) = {(O[j, 2] - plateau) * O[j, 0] ** 0.25:+.3e}",
                         flush=True)
print("DONE", flush=True)
