"""T357 (agent A, 20 Oct 2026): is the third of alpha lam_risk that the fixed-N closed form misses the CGMT feedback of
the extra variance into Vh and A1? cgmt_decompose.py showed the prox step does not matter at alpha 1000 (P = Q gives the same
lam_risk), so the fixed point reduces to two equations in (mu, sg):
    (ii)  mu = -A1 T1,   (iii)  mu^2 + sg^2 = A1^2 T2 + (E rho'^2 / n) T3,
    A1 = E[Z1 rho'(Q)] - mu Vh, Vh = E rho''(Q), Q = mu Z1 + sg Z2, G = 1/(lam + Vh S),
    T1 = sum mt^2 G / rho^2, T2 = sum mt^2 S G^2 / rho^2, T3 = sum S^2 G^2.
FULL solves (ii)-(iii) as they stand. FROZEN solves the n = inf system (no noise term) and then only adds the noise to sg^2 with
Vh, A1 and E rho'^2 held at their n = inf values - the variance with no feedback, which is what a fixed-N M-estimator
expansion keeps. MU_ONLY keeps the feedback in (ii) but not in (iii)'s A1^2 T2 term, to split the feedback further.
The minimiser of the excess risk over lam is alpha lam_risk for each. argv: beta alpha psi d [seed0]"""
import sys, math
import numpy as np
from scipy.optimize import root
beta, alpha, psi = map(float, sys.argv[1:4]); d = int(sys.argv[4]); seed0 = int(sys.argv[5]) if len(sys.argv) > 5 else 100
n = alpha * d; N = int(psi * d)
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); sp = lambda t: np.logaddexp(0, t)
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
gx, gw = np.polynomial.hermite_e.hermegauss(80); gw = gw / gw.sum()
Z1 = gx[:, None]; Z2 = gx[None, :]; W = gw[:, None] * gw[None, :]
bayes = ((sig(beta * gx) * sp(-beta * gx) + (1 - sig(beta * gx)) * sp(beta * gx)) * gw).sum()
def excess(q, cz):
    s_ = q * gx; mu_ = (cz / q ** 2) * s_[:, None]; sd = math.sqrt(max(1 - cz ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu_ + sd * gx[None, :])) * gw[None, :]).sum(1)
    return ((ey * sp(-s_) + (1 - ey) * sp(s_)) * gw).sum() - bayes
F = np.random.default_rng(seed0).standard_normal((N, d)) / math.sqrt(d)
ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); S = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
rho = math.sqrt((mt ** 2 / S).sum())
PY1 = (sig(beta * (rho * Z1[:, :, None] + math.sqrt(1 - rho ** 2) * gx[None, None, :])) * gw[None, None, :]).sum(2)
def moments(mu, sg):
    Q = mu * Z1 + sg * Z2; s_ = sig(Q); d2 = (W * s_ * (1 - s_)).sum()
    A = (W * Z1 * (s_ - PY1)).sum(); R2 = (W * (s_ * s_ - 2 * s_ * PY1 + PY1)).sum()
    return d2, A - mu * d2, R2
def Ts(lam, Vh):
    G = 1 / (lam + Vh * S)
    return (mt ** 2 * G).sum() / rho ** 2, (mt ** 2 * S * G ** 2).sum() / rho ** 2, (S ** 2 * G ** 2).sum()
def solve(lam, v0, noise, mode="full", frz=None):
    def eqs(v):
        mu, sg = v[0], math.exp(v[1]); Vh, A1, R2 = moments(mu, sg); T1, T2, T3 = Ts(lam, Vh)
        if mode == "mu_only":                                    # (iii)'s A1^2 T2 and the noise at the n = inf values
            T1f, T2f, T3f = Ts(lam, frz[0])
            return [(mu + A1 * T1) / max(abs(mu), 1e-12),
                    (mu ** 2 + sg ** 2 - frz[1] ** 2 * T2f - frz[2] / n * T3f) / (mu ** 2 + sg ** 2)]
        return [(mu + A1 * T1) / max(abs(mu), 1e-12), (mu ** 2 + sg ** 2 - A1 ** 2 * T2 - noise * R2 / n * T3) / (mu ** 2 + sg ** 2)]
    sol = root(eqs, v0, method="hybr", tol=1e-14)
    if max(abs(x) for x in eqs(sol.x)) > 1e-10:
        raise RuntimeError(f"no convergence at lam {lam:.4g} mode {mode}: {sol.message}")
    return sol.x
def lam_min(rows):
    r = np.array(rows); j = min(max(int(np.argmin(r[:, 1])), 1), len(r) - 2)
    P = np.polyfit(np.log(r[j - 1:j + 2, 0]), r[j - 1:j + 2, 1], 2)
    return (math.exp(-P[1] / (2 * P[0])) if P[0] > 0 else float("nan")), r[:, 1].min(), j in (1, len(r) - 2)
print(__doc__); print(f"beta {beta} alpha {alpha} N {N} d {d} n {n:.0f} seed0 {seed0}: rho {rho:.4f}", flush=True)
# walk the n = inf solution down from a large lam to the scan range
kap = (gw * gx * PY1[:, 0]).sum(); l0 = 10.0
v = np.array([kap * (mt ** 2 / (l0 + 0.25 * S)).sum() / rho ** 2,
              math.log(math.sqrt(1e-6 + 0.25 / n * (S ** 2 / (l0 + 0.25 * S) ** 2).sum()))])
for lam in np.exp(np.linspace(math.log(10), math.log(0.3 / alpha), 120)):
    v = solve(lam, v, 0)
lams = np.exp(np.linspace(math.log(0.3 / alpha), math.log(0.003 / alpha), 81))
res = {"full": [], "frozen": [], "mu_only": [], "ninf": []}
vf = v.copy(); vm = v.copy(); aux = []
for lam in lams:
    v = solve(lam, v, 0); mu0, sg0 = v[0], math.exp(v[1]); Vh0, A10, R20 = moments(mu0, sg0)
    res["ninf"].append((lam, excess(math.hypot(mu0, sg0), rho * mu0))); aux.append((lam, Vh0, R20))
    T1, T2, T3 = Ts(lam, Vh0); sgf = math.sqrt(sg0 ** 2 + R20 / n * T3)
    res["frozen"].append((lam, excess(math.hypot(mu0, sgf), rho * mu0)))
    vf = solve(lam, vf, 1); mu, sg = vf[0], math.exp(vf[1]); res["full"].append((lam, excess(math.hypot(mu, sg), rho * mu)))
    vm = solve(lam, vm, 1, "mu_only", (Vh0, A10, R20)); mu, sg = vm[0], math.exp(vm[1])
    res["mu_only"].append((lam, excess(math.hypot(mu, sg), rho * mu)))
for k in ("full", "frozen", "mu_only"):
    lr, ex, edge = lam_min(res[k])
    print(f"  {k:8s}: alpha*lam_risk {alpha * lr:.5f}  min excess {ex:.6e}" + ("  (minimum at the grid edge)" if edge else ""), flush=True)
r0 = np.array(res["ninf"]); print(f"  n = inf excess at the smallest/largest lam: {r0[-1, 1]:.6e} / {r0[0, 1]:.6e} (must rise with lam)")
# Closed form of the FROZEN minimiser. With dE/d(sg^2) = Vh/2 (Stein), E = E0(lam) + (1/n) g(lam) T3(lam), g = R2 Vh / 2, so
#   lam_frozen = -(1/n) [g T3' + g' T3] / kappa2,   T3(0) = N / Vh^2, T3'(0) = -2 sum 1/(Vh^3 S),
# kappa2 = E0''(0). The first term alone is the fixed-N variance term psi mean(1/s) E rho'^2 / Vh^2 / kappa2; g' is the change of the
# Hessian weight and of E rho'^2 along the n = inf regularisation path.
A = np.array(aux); E0 = np.array(res["ninf"])[:, 1]; lam_ = A[:, 0]
k2 = 2 * np.polyfit(lam_, E0, 2)[0]
gg = A[:, 2] * A[:, 1] / 2; gp = np.polyfit(lam_, gg, 1)[0]; g0 = np.polyval(np.polyfit(lam_, gg, 1), 0.0)
Vh0 = np.polyval(np.polyfit(lam_, A[:, 1], 1), 0.0); R20 = np.polyval(np.polyfit(lam_, A[:, 2], 1), 0.0)
t1 = g0 * 2 * (1 / S).sum() / Vh0 ** 3 / n / k2; t2 = -gp * N / Vh0 ** 2 / n / k2
print(f"  closed form (frozen): kappa2 {k2:.2f}  Vh {Vh0:.5f}  E rho'^2 {R20:.5f}  g' {gp:+.4f}  "
      f"alpha*lam: variance term {alpha * t1:.5f} + path term {alpha * t2:+.5f} = {alpha * (t1 + t2):.5f}", flush=True)
# The first version above held T3 at Vh(0): T3 also moves with Vh(lam). Numerical check of the same formula with T3 along the path:
T3p = np.array([Ts(l, vh)[2] for l, vh in zip(lam_, A[:, 1])]); VT = gg * T3p
vt1 = np.polyfit(lam_, VT, 1)[0]; Vhp = np.polyfit(lam_, A[:, 1], 1)[0]; R2p = np.polyfit(lam_, A[:, 2], 1)[0]
print(f"  frozen, (g T3)' along the path: alpha*lam = {-alpha * vt1 / n / k2:.5f}   (Vh' {Vhp:+.4f}, E rho'^2' {R2p:+.4f}; "
      f"kappa2 {k2:.2f} from the n = inf curve)", flush=True)
r1 = np.array(res["frozen"]); print("  frozen excess - n=inf excess at three lam:", " ".join(f"{l:.3g}:{e:.6e}" for l, e in
      zip(r1[::40, 0], r1[::40, 1] - E0[::40])), " predicted (1/n) g T3:", " ".join(f"{x / n:.6e}" for x in VT[::40]))
# Local version: the zero of E0' + (g T3)'/n on the grid itself (no straight-line fits), and the split of (g T3)' at that point
dE0 = np.gradient(E0, lam_); dVT = np.gradient(VT, lam_); f = dE0 + dVT / n; k = np.where(np.sign(f[:-1]) != np.sign(f[1:]))[0]
if len(k):
    k = k[0]; ls = lam_[k] - f[k] * (lam_[k + 1] - lam_[k]) / (f[k + 1] - f[k])
    dg = np.gradient(gg, lam_); dT3 = np.gradient(T3p, lam_); w = (ls - lam_[k]) / (lam_[k + 1] - lam_[k]); at = lambda a: a[k] + w * (a[k + 1] - a[k])
    print(f"  local zero of E0' + (gT3)'/n: alpha*lam = {alpha * ls:.5f}; there (gT3)' = g T3' {at(gg) * at(dT3):+.4e} + g' T3 {at(dg) * at(T3p):+.4e}, "
          f"E0'/lam {at(dE0) / ls:.2f}", flush=True)
