"""T357, gradient descent: where OC = 0 falls on GD's path against FM = 0 and the risk optimum.
Claim tested (calibration half). Near the MLE the flow contracts along w* at rate i_par = E z^2 sig'(beta z) and across it at
i_perp = E sig'(beta z) > i_par, so late on kappa(t) = kappa_hat - K0 exp(-i_par t) while alpha |w_perp|^2 is C up to a relative
O(exp(-i_perp t)). OC = 0 and FM = 0 are zero crossings of O(1/alpha) functionals of (kappa, |w_perp|^2), so to leading order they
sit where ridge's do on the kappa axis, and
    t_FM - t_OC -> ln(lam_OC/lam_FM)/i_par    (0.473 at beta 2, 8.150 at beta 5; lam_FM = lam_risk for ridge, oc_limit_run1.txt).
The risk optimum is NOT predicted by this: ridge's gain comes partly from shrinking w_perp, which GD has already converged, and that
enters the risk at the same order as the kappa shift. t_risk is reported for the record only.
GD: step 0.1 from 0 on the logistic loss, read on a grid of every step; zero crossings by linear interpolation, t_risk from a parabola
through the excess risk around its minimum. OC and FM are integrated with Gauss-Legendre on the half line (the integrands are odd;
Hermite nodes across the sign kink converge slowly).
argv: d alpha beta seeds tmax [ratio]"""
import sys, math
import numpy as np
d = int(sys.argv[1]); alpha = float(sys.argv[2]); beta = float(sys.argv[3]); seeds = int(sys.argv[4]); tmax = float(sys.argv[5])
ratio = float(sys.argv[6]) if len(sys.argv) > 6 else float("nan")
n = int(alpha * d); ETA = 0.1
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); softplus = lambda t: np.logaddexp(0, t)
hx, hw = np.polynomial.hermite_e.hermegauss(80); hw = hw / hw.sum()
lx, lw = np.polynomial.legendre.leggauss(200); lx = 5 * (lx + 1); lw = 5 * lw * np.exp(-lx ** 2 / 2) / math.sqrt(2 * math.pi)  # u in [0, 10]
ux = np.concatenate([-lx[::-1], lx]); uw = np.concatenate([lw[::-1], lw])


def pop(q, c):
    s = q * ux; mu = (c / q ** 2) * s[:, None]; sd = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu + sd * hx[None, :])) * hw[None, :]).sum(1); p = sig(s)
    oc = ((p - ey) * np.sign(s) * uw).sum(); fm = ((p - ey) * s * uw).sum()
    risk = ((ey * softplus(-s) + (1 - ey) * softplus(s)) * uw).sum()
    return oc, fm, risk


sp = sig(beta * hx) * (1 - sig(beta * hx)); ipar = (hw * hx ** 2 * sp).sum()
pred = math.log(ratio) / ipar if ratio == ratio else float("nan")
rows = []
for sd in range(seeds):
    rng = np.random.default_rng(100 + sd)
    X = rng.standard_normal((n, d)); s = np.where(rng.random(n) < sig(beta * X[:, 0]), 1.0, -1.0)
    w = np.zeros(d); T, OC, FM, RK = [], [], [], []
    for k in range(1, int(tmax / ETA) + 1):
        m = s * (X @ w); w = w + ETA * (X.T @ (s * sig(-m))) / n
        if k % 1 == 0 and k * ETA > 2:
            o, f, r = pop(float(np.linalg.norm(w)), float(w[0])); T.append(k * ETA); OC.append(o); FM.append(f); RK.append(r)
    T, OC, FM, RK = map(np.array, (T, OC, FM, RK))
    def cross(Y):
        j = np.where((Y[:-1] < 0) & (Y[1:] >= 0))[0]
        return T[j[0]] - Y[j[0]] * (T[j[0] + 1] - T[j[0]]) / (Y[j[0] + 1] - Y[j[0]]) if len(j) else float("nan")
    t_oc, t_fm = cross(OC), cross(FM)
    i = int(np.argmin(RK)); lo, hi = max(i - 40, 0), min(i + 41, len(T))
    a = np.polyfit(T[lo:hi] - T[i], RK[lo:hi], 2); t_r = T[i] - a[1] / (2 * a[0])
    rows.append((t_fm - t_oc, t_r - t_fm))
    print(f"  seed {sd}: t_OC {t_oc:.3f}  t_FM {t_fm:.3f}  t_risk {t_r:.3f} (grid {T[i]:.1f})  t_FM-t_OC {t_fm - t_oc:+.3f}  t_risk-t_FM {t_r - t_fm:+.3f}"
          f"{'  RISK MIN AT END' if T[i] >= T[-1] - 1 else ''}", flush=True)
g = np.array([r[0] for r in rows]); h = np.array([r[1] for r in rows]); se = lambda a: a.std(ddof=1) / math.sqrt(len(a)) if len(a) > 1 else 0
print(f"d={d} alpha={alpha} beta={beta} seeds={seeds}: t_FM-t_OC mean {g.mean():+.4f} se {se(g):.4f} (predicted alpha->inf {pred:+.3f})"
      f"  t_risk-t_FM mean {h.mean():+.3f} se {se(h):.3f}  i_par {ipar:.5f}", flush=True)
