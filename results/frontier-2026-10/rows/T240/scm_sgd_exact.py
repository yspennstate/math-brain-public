"""Exact finite-N online SGD for the K=M=2 erf soft committee (noiseless, output weights 1), run on its order parameters.

One SGD step w_i <- w_i + (eta/sqrt N) d_i x, d_i = g'(h_i)(y - f), depends on x only through u = (h_1, h_2, y_1, y_2)
(the student and teacher fields, u ~ N(0, C) with C the 4x4 overlap matrix) and |x|^2/N. Writing u = L z with
L L^T = C and z ~ N(0, I_4), the part of x in the span of the four vectors has squared length |z|^2 and the rest is an
independent chi-square with N - 4 degrees of freedom. So the overlaps evolve exactly as
    Q_ik += (eta/N)(d_i h_k + d_k h_i) + (eta^2/N) d_i d_k (|z|^2 + chi2_{N-4})/N,   R_in += (eta/N) d_i y_n,
a Markov chain on seven numbers whose law is that of the N-dimensional SGD (no approximation). A step costs O(1) in N,
so N = 10^5 is as cheap per unit of time as N = 500 is per step.
Start: w_i i.i.d. uniform on the sphere of radius sqrt(N q0), teacher v_n = sqrt(N) e_n; the initial overlaps are drawn
from that law directly. tau_N = first time t = steps/N, read every N/10 steps, with |R_11 - R_12| > delta (as in
scm_sgd_escape.py, the brute-force check of this file).
usage: python -X utf8 scm_sgd_exact.py eta runs N [N ...]"""
import sys
import time
import numpy as np
from scipy.special import erf

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

eta = float(sys.argv[1])
runs = int(sys.argv[2])
Ns = [int(a) for a in sys.argv[3:]]
q0, delta, tmax = 0.2, 0.2, 3000.0
c = np.sqrt(2 / np.pi)
rng = np.random.default_rng(20261016 + 7)


def initial(N):
    # g_i ~ N(0, I_N); only the two teacher coordinates, |g_i|^2 and g_1.g_2 matter
    a = rng.standard_normal((runs, 2, 2))              # coordinates on e_1, e_2
    rest1 = rng.chisquare(N - 2, runs)                  # |g_1 perp|^2
    # g_2 perp = rho-part along g_1 perp + independent: g_1perp . g_2perp = sqrt(rest1) * N(0,1)
    cross = np.sqrt(rest1) * rng.standard_normal(runs)
    rest2 = cross ** 2 / rest1 + rng.chisquare(N - 3, runs)
    n1 = np.sqrt((a[:, 0] ** 2).sum(1) + rest1)
    n2 = np.sqrt((a[:, 1] ** 2).sum(1) + rest2)
    Q = np.empty((runs, 2, 2))
    Q[:, 0, 0] = q0
    Q[:, 1, 1] = q0
    Q[:, 0, 1] = Q[:, 1, 0] = q0 * ((a[:, 0] * a[:, 1]).sum(1) + cross) / (n1 * n2)
    R = np.sqrt(q0) * a / np.stack([n1, n2], 1)[:, :, None]
    return Q, R


def run(N):
    Q, R = initial(N)
    tau = np.full(runs, np.nan)
    C = np.zeros((runs, 4, 4))
    C[:, 2:, 2:] = np.eye(2)
    steps = int(tmax * N)
    chk = max(N // 10, 1)
    for s in range(steps):
        C[:, :2, :2] = Q
        C[:, :2, 2:] = R
        C[:, 2:, :2] = np.transpose(R, (0, 2, 1))
        L = np.linalg.cholesky(C)
        z = rng.standard_normal((runs, 4))
        u = np.einsum("rij,rj->ri", L, z)
        h, y = u[:, :2], u[:, 2:]
        err = erf(y / np.sqrt(2)).sum(1) - erf(h / np.sqrt(2)).sum(1)
        d = c * np.exp(-h * h / 2) * err[:, None]
        x2 = ((z * z).sum(1) + rng.chisquare(N - 4, runs)) / N
        Q += (eta / N) * (d[:, :, None] * h[:, None, :] + h[:, :, None] * d[:, None, :]) \
            + (eta * eta / N) * d[:, :, None] * d[:, None, :] * x2[:, None, None]
        R += (eta / N) * d[:, :, None] * y[:, None, :]
        if s % chk == 0:
            new = np.isnan(tau) & (np.abs(R[:, 0, 0] - R[:, 0, 1]) > delta)
            tau[new] = s / N
            if not np.isnan(tau).any():
                break
    return tau


res = {}
for N in Ns:
    t0 = time.time()
    tau = run(N)
    res[N] = tau
    print("N %6d: tau median %.1f, mean %.2f, sd %.1f, se %.2f, unescaped %d/%d (%.0f s)"
          % (N, np.nanmedian(tau), np.nanmean(tau), np.nanstd(tau), np.nanstd(tau) / np.sqrt(runs),
             np.isnan(tau).sum(), runs, time.time() - t0), flush=True)
if len(Ns) > 1:
    L_ = np.log(np.array(Ns, float))
    m = np.array([np.nanmean(res[N]) for N in Ns])
    se = np.array([np.nanstd(res[N]) / np.sqrt(runs) for N in Ns])
    W = 1 / se ** 2
    A = np.vstack([L_, np.ones_like(L_)]).T
    cov = np.linalg.inv(A.T @ (A * W[:, None]))
    beta = cov @ (A.T @ (W * m))
    print("weighted fit mean tau = %.2f (+- %.2f) * log N + %.1f   (ODE prediction for the slope: %.2f)"
          % (beta[0], np.sqrt(cov[0, 0]), beta[1], 1 / (2 * 0.0316182)), flush=True)
