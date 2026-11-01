"""T255: one-step drift and variance of a = tr(P V)/(m-1) on the exchangeable ray V = a I + c 11^T, from the exact chain
(chain_blowup.py's step) at large n, against the formulas
  drift  n E[da]   -> kappa a^3,  kappa = gam^2 (m-1)/(tau0^2 m^2)
  var    n Var[da] -> 2 gam^2 (2 - gam^2) a^2/(m-1)   (linear part)   +   4 gam^4 a^4/(tau0^2 m^2 (m-1))   (attention part)
usage: python -X utf8 ray_check.py"""
import numpy as np

rng = np.random.default_rng(7)


def step_stats(V, gam2, n, reps, nk=1, tau0=1.0):
    m = V.shape[0]; lam, gam = np.sqrt(1 - gam2), np.sqrt(gam2); tau = tau0 * np.sqrt(n * nk)
    L = np.linalg.cholesky(V); I = np.eye(m); J = np.ones((m, m)) / m; P = I - J
    out = []
    for _ in range(reps // 20000):
        k = 20000
        G1 = rng.standard_normal((k, m, nk)); G2 = rng.standard_normal((k, m, nk))
        Y = L @ G1 @ np.swapaxes(G2, 1, 2) @ L.T
        Zs = Y / tau; Zs = Zs - Zs.max(2, keepdims=True); E = np.exp(Zs); A = I + E / E.sum(2, keepdims=True) - J
        Z = rng.standard_normal((k, m, m))
        AT = np.swapaxes(A, 1, 2)
        cross = L @ np.swapaxes(Z, 1, 2) @ L.T @ AT
        GG = Z @ np.swapaxes(Z, 1, 2) + (n - m) * I + np.sqrt(2 * (n - m)) * 0  # mean of the Wishart part; its fluctuation added below
        Wf = rng.standard_normal((k, m, m)) * np.sqrt(n - m)          # Wishart(m, n-m) = (n-m) I + sqrt(n-m) (H + H^T)/sqrt2-ish to leading order
        Wf = (Wf + np.swapaxes(Wf, 1, 2)) / np.sqrt(2)
        Vn = lam ** 2 * V + (lam * gam / np.sqrt(n)) * (cross + np.swapaxes(cross, 1, 2)) + (gam2 / n) * (A @ L @ (GG + Wf) @ L.T @ AT)
        da = (np.einsum('ij,kij->k', P, Vn) - np.sum(P * V)) / (m - 1)
        out.append(da)
    da = np.concatenate(out)
    return n * da.mean(), n * da.var(), np.sqrt(n * n * da.var() / len(da))


for m, gam2, a, c in ((4, 0.5, 8.0, 2.0), (4, 0.5, 2.0, 0.5), (3, 0.5, 8.0, 2.0), (2, 0.5, 8.0, 2.0)):
    V = a * np.eye(m) + c * np.ones((m, m))
    n = 10 ** 6
    mu, var, se = step_stats(V, gam2, n, 400000)
    kap = gam2 * (m - 1) / m ** 2
    vlin = 2 * gam2 * (2 - gam2) * a ** 2 / (m - 1); vatt = 4 * gam2 ** 2 * a ** 4 / (m ** 2 * (m - 1))
    print("m %d gam2 %.1f a %.1f c %.1f: n E[da] %.2f +- %.2f (kappa a^3 = %.2f) | n Var[da] %.1f (formula %.1f = lin %.1f + att %.1f)" % (
        m, gam2, a, c, mu, se, kap * a ** 3, var, vlin + vatt, vlin, vatt), flush=True)
