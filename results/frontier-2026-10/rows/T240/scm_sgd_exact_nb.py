"""Numba version of scm_sgd_exact.py (same exact order-parameter chain, one run at a time, a few hundred ns a step).

The teacher fields are y ~ N(0, I_2); given y the student fields are h = R y + chol(Q - R R^T) xi with xi ~ N(0, I_2),
and |x|^2/N = (|y|^2 + |xi|^2 + chi2_{N-4})/N. Also records, per run, the time the transverse coordinate first exceeds
each threshold in GAPS, so the growth rate can be read off the gaps (slope of log gap in time) as well as off N.
usage: python -X utf8 scm_sgd_exact_nb.py eta runs N [N ...]"""
import sys
import math
import time
import numpy as np
import numba

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

GAPS = np.array([0.0125, 0.025, 0.05, 0.1, 0.2])
C0 = math.sqrt(2 / math.pi)
S2 = math.sqrt(2.0)


@numba.njit(cache=True)
def one(N, eta, q0, tmax, seed, gaps):
    np.random.seed(seed)
    # initial overlaps of w_i uniform on the sphere of radius sqrt(N q0); teacher v_n = sqrt(N) e_n
    a11, a12, a21, a22 = np.random.normal(), np.random.normal(), np.random.normal(), np.random.normal()
    rest1 = 2.0 * np.random.gamma((N - 2) / 2.0)
    cr = math.sqrt(rest1) * np.random.normal()
    g = np.random.normal()
    rest2 = g * g + 2.0 * np.random.gamma((N - 3) / 2.0)
    n1 = math.sqrt(a11 * a11 + a12 * a12 + rest1)
    n2 = math.sqrt(a21 * a21 + a22 * a22 + rest2)
    Q11 = q0
    Q22 = q0
    Q12 = q0 * (a11 * a21 + a12 * a22 + cr) / (n1 * n2)
    sq = math.sqrt(q0)
    R11, R12, R21, R22 = sq * a11 / n1, sq * a12 / n1, sq * a21 / n2, sq * a22 / n2
    out = np.full(gaps.shape[0], np.nan)
    k = 0
    steps = int(tmax * N)
    chk = max(N // 10, 1)
    for s in range(steps):
        y1 = np.random.normal()
        y2 = np.random.normal()
        x1 = np.random.normal()
        x2 = np.random.normal()
        s11 = Q11 - R11 * R11 - R12 * R12
        s12 = Q12 - R11 * R21 - R12 * R22
        s22 = Q22 - R21 * R21 - R22 * R22
        l11 = math.sqrt(max(s11, 1e-300))
        l21 = s12 / l11
        l22 = math.sqrt(max(s22 - l21 * l21, 0.0))
        h1 = R11 * y1 + R12 * y2 + l11 * x1
        h2 = R21 * y1 + R22 * y2 + l21 * x1 + l22 * x2
        err = math.erf(y1 / S2) + math.erf(y2 / S2) - math.erf(h1 / S2) - math.erf(h2 / S2)
        d1 = C0 * math.exp(-h1 * h1 / 2) * err
        d2 = C0 * math.exp(-h2 * h2 / 2) * err
        xx = (y1 * y1 + y2 * y2 + x1 * x1 + x2 * x2 + 2.0 * np.random.gamma((N - 4) / 2.0)) / N
        e = eta / N
        e2 = eta * eta / N * xx
        Q11 += e * 2 * d1 * h1 + e2 * d1 * d1
        Q12 += e * (d1 * h2 + d2 * h1) + e2 * d1 * d2
        Q22 += e * 2 * d2 * h2 + e2 * d2 * d2
        R11 += e * d1 * y1
        R12 += e * d1 * y2
        R21 += e * d2 * y1
        R22 += e * d2 * y2
        if s % chk == 0:
            gp = abs(R11 - R12)
            while k < gaps.shape[0] and gp > gaps[k]:
                out[k] = s / N
                k += 1
            if k == gaps.shape[0]:
                break
    return out


if __name__ == "__main__":
    eta = float(sys.argv[1])
    runs = int(sys.argv[2])
    Ns = [int(a) for a in sys.argv[3:]]
    res = {}
    for N in Ns:
        t0 = time.time()
        T = np.array([one(N, eta, 0.2, 4000.0, 1000003 * N + r, GAPS) for r in range(runs)])
        res[N] = T
        tau = T[:, -1]
        print("N %6d: tau(0.2) median %.1f mean %.2f sd %.1f se %.2f unescaped %d/%d | mean t at gaps %s (%.0f s)"
              % (N, np.nanmedian(tau), np.nanmean(tau), np.nanstd(tau), np.nanstd(tau) / np.sqrt(runs),
                 np.isnan(tau).sum(), runs, " ".join("%.1f" % v for v in np.nanmean(T, 0)), time.time() - t0), flush=True)
    if len(Ns) > 1:
        L_ = np.log(np.array(Ns, float))
        m = np.array([np.nanmean(res[N][:, -1]) for N in Ns])
        se = np.array([np.nanstd(res[N][:, -1]) / np.sqrt(runs) for N in Ns])
        W = 1 / se ** 2
        A = np.vstack([L_, np.ones_like(L_)]).T
        cov = np.linalg.inv(A.T @ (A * W[:, None]))
        beta = cov @ (A.T @ (W * m))
        print("weighted fit mean tau = %.2f (+- %.2f) * log N + %.1f   (ODE prediction for the slope at eta 0.5: %.2f)"
              % (beta[0], np.sqrt(cov[0, 0]), beta[1], 1 / (2 * 0.0316182)), flush=True)
