"""T255: hitting times of large covariance for the finite shaped-attention network (Noci et al. 2306.17759, Eq. 1 + Eq. 9),
simulated EXACTLY through its covariance Markov chain V_l = X_l X_l^T / n:
  given V = L L^T, with Z (m x m) iid N(0,1), W' ~ Wishart(m, n - m), G1, G2 (m x nk) iid N(0,1) independent,
  Y = L G1 G2^T L^T, A = I + Softmax(Y / (tau0 sqrt(n nk))) - 11^T/m,
  V' = lam^2 V + (lam gam / sqrt n)(L Z^T L^T A^T + A L Z L^T) + (gam^2 / n) A L (Z Z^T + W') L^T A^T.
(derivation: X = L Q with Q Q^T = n I; X W^V / sqrt n = L G with G = Q W^V / sqrt n iid; Q G^T = sqrt n Z^T.)
Time t = l / n. Reports, per (m, gam^2, n), the fraction of runs whose mean diagonal reached 10 and 100 by t = T, and
the median hitting times. Theory (exchangeable ray, Feller test): explosion iff (m - 1)^2 > 2 gam^2.
usage: python -X utf8 chain_blowup.py m gam2 n T reps [rho0] [nk]"""
import sys
import numpy as np

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

m = int(sys.argv[1]); gam2 = float(sys.argv[2]); n = int(sys.argv[3]); T = float(sys.argv[4]); R = int(sys.argv[5])
rho0 = float(sys.argv[6]) if len(sys.argv) > 6 else 0.2
nk = int(sys.argv[7]) if len(sys.argv) > 7 else 1
tau0 = 1.0
lam, gam = np.sqrt(1 - gam2), np.sqrt(gam2)
tau = tau0 * np.sqrt(n * nk)
rng = np.random.default_rng(12345 + 7 * m + n)
V = np.broadcast_to((1 - rho0) * np.eye(m) + rho0, (R, m, m)).copy()
alive = np.ones(R, bool)
hit10 = np.full(R, np.inf); hit100 = np.full(R, np.inf); low = np.full(R, np.inf)
I = np.eye(m); J = np.ones((m, m)) / m
steps = int(T * n)
il = np.tril_indices(m, -1)


def wishart(k, size):
    # Bartlett: W = B B^T, B lower, B_ii ~ sqrt(chi2(k - i)), B_ij ~ N(0,1) below the diagonal
    B = np.zeros((size, m, m))
    for i in range(m):
        B[:, i, i] = np.sqrt(rng.chisquare(k - i, size))
    B[:, il[0], il[1]] = rng.standard_normal((size, len(il[0])))
    return B @ np.swapaxes(B, 1, 2)


for step in range(1, steps + 1):
    idx = np.nonzero(alive)[0]
    if len(idx) == 0:
        break
    Va = V[idx]
    k = len(idx)
    try:
        L = np.linalg.cholesky(Va)
    except np.linalg.LinAlgError:
        Va = Va + 1e-12 * I; L = np.linalg.cholesky(Va)
    G1 = rng.standard_normal((k, m, nk)); G2 = rng.standard_normal((k, m, nk))
    Y = L @ G1 @ np.swapaxes(G2, 1, 2) @ np.swapaxes(L, 1, 2)
    Zs = Y / tau
    Zs = Zs - Zs.max(2, keepdims=True)
    E = np.exp(Zs); A = I + E / E.sum(2, keepdims=True) - J
    Z = rng.standard_normal((k, m, m))
    LT = np.swapaxes(L, 1, 2); AT = np.swapaxes(A, 1, 2)
    cross = L @ np.swapaxes(Z, 1, 2) @ LT @ AT
    GG = Z @ np.swapaxes(Z, 1, 2) + wishart(n - m, k)
    Vn = lam ** 2 * Va + (lam * gam / np.sqrt(n)) * (cross + np.swapaxes(cross, 1, 2)) + (gam2 / n) * (A @ L @ GG @ LT @ AT)
    V[idx] = Vn
    t = step / n
    md = np.trace(Vn, axis1=1, axis2=2) / m
    j = idx[(md >= 10) & np.isinf(hit10[idx])]; hit10[j] = t
    j = idx[(md >= 100)]; hit100[j] = t; alive[j] = False
    j = idx[(md <= 0.01) & np.isinf(low[idx])]; low[j] = t
    if step % max(1, steps // 8) == 0:
        print("  t %.2f alive %d  hit10 %d hit100 %d  low(0.01) %d  median mean-diag %.3g" % (
            t, alive.sum(), np.isfinite(hit10).sum(), np.isfinite(hit100).sum(), np.isfinite(low).sum(),
            np.median(np.trace(V, axis1=1, axis2=2) / m)), flush=True)


def med(h):
    f = h[np.isfinite(h)]
    return "%.2f" % np.median(f) if len(f) else "-"


k_feller = (m - 1) ** 2 / (2 * gam2)
print("m %d gam2 %.2f n %d nk %d rho0 %.2f T %.1f reps %d | (m-1)^2/(2 gam^2) = %.2f | P(hit 10) %.3f med t %s | "
      "P(hit 100) %.3f med t %s | P(mean diag <= 0.01) %.3f" % (
          m, gam2, n, nk, rho0, T, R, k_feller, np.isfinite(hit10).mean(), med(hit10), np.isfinite(hit100).mean(),
          med(hit100), np.isfinite(low).mean()), flush=True)
