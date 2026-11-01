"""T357: test the path lemma. Along any path (q(t), rho(t)) with q increasing, write R(q, rho) for the population logistic risk of
a linear predictor of norm q and alignment rho = c/q. At the path's risk minimum, 0 = R_q q' + R_rho rho'. If R_rho < 0 and q' > 0,
then sign(R_q) = sign(rho'): the risk-optimal fit is over-scaled (first-moment over-confident, R_q > 0) exactly when the alignment is
still rising there. q R_q = FM := E[(sigma(zhat) - y) zhat], the first-moment calibration. Prediction: lam_fm > lam_risk iff
lam_rho < lam_risk (lam_rho = argmax of rho), and on GD t_fm < t_risk iff t_rho > t_risk. Also checks R_rho < 0 at every path point
and how far the OC root (lam_cal) sits from the FM root (lam_fm).
Exact identity behind it (Stein): zhat ~ N(0, q^2) always, so R(q, c) = A(q) - kappa_beta c with A(q) = E softplus(q g) and
kappa_beta = E[sigma(beta g) g]; hence FM = q A'(q) - kappa c, and at a stationary point of R along the path FM = kappa q^2 drho/dq.
The optimum is located by a quadratic fit in log(time) and drho/dq by a quadratic fit of rho on q (7 points).
argv: d alpha beta seeds T(GD steps) ; env ETA (GD step, default 0.1)
"""
import sys, math, os
import numpy as np
T = int(sys.argv[5]); ETA = float(os.environ.get("ETA", "0.1"))
sys.argv = sys.argv[:1] + sys.argv[1:5] + ["1"]
exec(open("calib_path.py", encoding="utf-8").read().split('print(f"d={d}')[0])

def fm_risk(q, rho):
    s = q * gh_x; mu = rho * gh_x[:, None]; sd = math.sqrt(max(1 - rho ** 2, 0))   # z*|u ~ N(rho u, 1 - rho^2), u = zhat/q
    ey = (sig(beta * (mu + sd * gh_x[None, :])) * gh_w[None, :]).sum(1); p = sig(s)
    fm = ((p - ey) * s * gh_w).sum()
    risk = ((ey * softplus(-s) + (1 - ey) * softplus(s)) * gh_w).sum()
    oc = ((p - ey) * np.sign(p - 0.5) * gh_w).sum()
    return fm, risk, oc

def path_stats(P):                  # P rows: (time-like, q, rho), ordered by q increasing
    F = np.array([fm_risk(q, r) for _, q, r in P]); fm, R, oc = F[:, 0], F[:, 1], F[:, 2]
    h = 1e-4; Rr = np.array([(fm_risk(q, min(r + h, 1 - 1e-9))[1] - fm_risk(q, r - h)[1]) / (2 * h) for _, q, r in P])
    def root(v):
        i = np.where((v[:-1] < 0) & (v[1:] >= 0))[0]
        if not len(i): return float("nan")
        i = i[0]; f = -v[i] / (v[i + 1] - v[i]); return P[i, 0] + f * (P[i + 1, 0] - P[i, 0])
    j = int(np.argmin(R)); k = int(np.argmax(P[:, 2]))
    # continuous optimum: quadratic fit of R in log(time-like) on 7 points around the grid argmin
    lo, hi = max(j - 3, 0), min(j + 4, len(P)); x = np.log(P[lo:hi, 0])
    a2, a1, a0 = np.polyfit(x, R[lo:hi], 2); xs = -a1 / (2 * a2)
    qs = np.polyval(np.polyfit(x, P[lo:hi, 1], 2), xs); rs = np.polyval(np.polyfit(x, P[lo:hi, 2], 2), xs)
    b = np.polyfit(P[lo:hi, 1], P[lo:hi, 2], 2); drdq = 2 * b[0] * qs + b[1]           # path slope d rho / d q at the optimum
    fms = fm_risk(qs, rs)[0]
    return math.exp(xs), P[k, 0], root(fm), root(oc), fms, bool((Rr < 0).all()), qs, rs, KAP * qs ** 2 * drdq

KAP = float((sig(beta * gh_x) * gh_x * gh_w).sum())     # kappa_beta = E[sigma(beta g) g]
res_r, res_g = [], []
lgrid = np.exp(np.linspace(math.log(10), math.log(1e-3), 90))
ts = sorted(set(np.unique(np.round(np.exp(np.linspace(0, math.log(T), 150))).astype(int))))
for sd in range(seeds):
    rng = np.random.default_rng(sd)
    X = rng.standard_normal((n, d)); wstar = np.zeros(d); wstar[0] = 1.0
    s = np.where(rng.random(n) < sig(beta * X[:, 0]), 1.0, -1.0)
    w = np.zeros(d); P = []
    for lam in lgrid:
        w = fit(X, s, lam, w); q = float(np.linalg.norm(w)); P.append((lam, q, float(w @ wstar) / q))
    res_r.append(path_stats(np.array(P)))
    w = np.zeros(d); P = []; k = 0
    for t in ts:
        while k < t:
            m = s * (X @ w); w = w + ETA * (X.T @ (s * sig(-m))) / n; k += 1
        q = float(np.linalg.norm(w)); P.append((t * ETA, q, float(w @ wstar) / q))
    res_g.append(path_stats(np.array(P)))
for name, res, rel in (("ridge lam", res_r, ">"), ("GD time", res_g, "<")):
    for r in res:
        risk, rhoarg, fmr, ocr, fmj, rneg, qj, rj, pred_fm = r
        pred = pred_fm > 0                                                             # alignment still rising (in q) at the risk optimum
        got = (fmr > risk) if name.startswith("ridge") else (fmr < risk)
        print(f"alpha={alpha} beta={beta} {name}: risk-opt {risk:.4g} rho-argmax(grid) {rhoarg:.4g} FM-root {fmr:.4g} OC-root {ocr:.4g} | "
              f"FM at risk-opt {fmj:+.5f} vs kappa q^2 drho/dq {pred_fm:+.5f} | R_rho<0 on path {rneg} | rising-at-opt {pred} FM-root {rel} risk-opt {got} | q,rho at opt {qj:.3f},{rj:.4f}", flush=True)
