"""T357 (agent A, 21 Oct 2026): deterministic equivalents of the spectral data in k_inf (cgmt_lam0_closed.py).
Sig = mu1^2 F F' + mus^2 I, F N x d with N(0, 1/d) entries, psi = N/d, t = mus^2/mu1^2, mt = V'(mu1 F e1). Let mu be the
Marchenko-Pastur law of F F' (ratio psi, atom 1 - 1/psi at 0 when psi > 1), m(z) its Stieltjes transform,
    m(z) = (1 - psi - z - sqrt((1 - psi - z)^2 - 4 psi z)) / (2 psi z),
and G(z) = e1'F'(F F' - z)^{-1} F e1. Since F'(FF' - z)^{-1}F = I + z (F'F - z)^{-1} and F'F is rotation invariant with law
psi mu + (1 - psi) delta_0, G(z) -> psi (1 + z m(z)), the transform of nu(dl) = psi l mu(dl). Hence, as d -> inf,
    mean(1/S) = m(-t)/mu1^2,   rho^2 = sum mt^2/S = G(-t),
    E_w(1/S) = G'(-t)/(mu1^2 G(-t)),   E_w(1/S^2) = G''(-t)/(2 mu1^4 G(-t)),   Var_w = E_w(1/S^2) - E_w(1/S)^2.
Checks: (1) these closed forms against a quadrature of mu (theta substitution, smooth at psi = 1); (2) the finite-d values
over several F seeds at two sizes (the quadratic forms fluctuate at order d^{-1/2}); (3) k_inf recomputed with the spectrum
replaced by the quadrature measure, against cgmt_lam0_closed at d 1000 seed 100. argv: beta psi [nodes]"""
import sys, math
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
beta, psi = float(sys.argv[1]), float(sys.argv[2]); K = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
t = mus2 / mu1 ** 2
print(__doc__)
mp.mp.dps = 40
def m_mp(z):
    z = mp.mpf(z); p = mp.mpf(psi)
    return (1 - p - z - mp.sqrt((1 - p - z) ** 2 - 4 * p * z)) / (2 * p * z)
G_mp = lambda z: psi * (1 + z * m_mp(z))
z0 = -t
G0, G1, G2 = (float(mp.diff(G_mp, z0, k)) for k in (0, 1, 2))
closed = dict(mean_invS=float(m_mp(z0)) / mu1 ** 2, rho2=G0, Ew=G1 / (mu1 ** 2 * G0),
              Ew2=G2 / (2 * mu1 ** 4 * G0))
closed["Varw"] = closed["Ew2"] - closed["Ew"] ** 2
print(f"beta {beta} psi {psi}: mu1 {mu1:.6f} mus^2 {mus2:.6f} t {t:.6f}")
print("closed forms:   " + "  ".join(f"{k} {v:.6f}" for k, v in closed.items()), flush=True)
# quadrature of mu: l = c + r cos(theta), density sqrt((b - l)(l - a)) / (2 pi psi l) on [a, b], plus the atom when psi > 1
a, b = (1 - math.sqrt(psi)) ** 2, (1 + math.sqrt(psi)) ** 2; c, r = (a + b) / 2, (b - a) / 2
gx, gw = np.polynomial.legendre.leggauss(K); th = 0.5 * math.pi * (gx + 1); thw = 0.5 * math.pi * gw
lam = c + r * np.cos(th)
om = thw * r * r * np.sin(th) ** 2 / (2 * math.pi * psi * lam)
if psi > 1:
    lam = np.append(lam, 0.0); om = np.append(om, 1 - 1 / psi)
S = mu1 ** 2 * lam + mus2; nu = mu1 ** 2 * psi * lam * om          # nu_k plays the role of mt_k^2
quad = dict(mean_invS=(om / S).sum(), rho2=(nu / S).sum())
w = nu / S / quad["rho2"]; quad["Ew"] = (w / S).sum(); quad["Ew2"] = (w / S ** 2).sum()
quad["Varw"] = quad["Ew2"] - quad["Ew"] ** 2
print(f"quadrature ({K} nodes, mass {om.sum():.12f}): " + "  ".join(f"{k} {v:.6f}" for k, v in quad.items()), flush=True)
# finite d
for d, seeds in ((1000, (100, 101, 102, 103, 104)), (3000, (100, 101))):
    N = int(psi * d); rows = []
    for sd in seeds:
        F = np.random.default_rng(sd).standard_normal((N, d)) / math.sqrt(d)
        ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); Sf = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
        rho2 = (mt ** 2 / Sf).sum(); wf = mt ** 2 / Sf / rho2; Ew = (wf / Sf).sum(); Ew2 = (wf / Sf ** 2).sum()
        rows.append(((1 / Sf).mean(), rho2, Ew, Ew2, Ew2 - Ew ** 2))
        print(f"  d {d} seed {sd}: mean_invS {rows[-1][0]:.6f}  rho2 {rho2:.6f}  Ew {Ew:.6f}  Ew2 {Ew2:.6f}  Varw {rows[-1][4]:.6f}",
              flush=True)
    R = np.array(rows)
    print(f"  d {d} mean over {len(seeds)} seeds: " + "  ".join(f"{k} {v:.6f}" for k, v in zip(closed, R.mean(0)))
          + "  | sd " + " ".join(f"{v:.4f}" for v in R.std(0, ddof=1) if len(seeds) > 1), flush=True)
# k_inf on the limiting measure: cgmt_lam0_closed.py with sum over N -> N sum om, sum mt^2 -> sum nu
d = 1000; N = psi * d
gx2, gw2 = np.polynomial.hermite_e.hermegauss(80); gw2 = gw2 / gw2.sum()
Z1 = gx2[:, None]; Z2 = gx2[None, :]; W = gw2[:, None] * gw2[None, :]
rho = math.sqrt(quad["rho2"])
PY1 = (sig(beta * (rho * Z1[:, :, None] + math.sqrt(1 - rho ** 2) * gx2[None, None, :])) * gw2[None, None, :]).sum(2)
def mom(mu, s):
    Q = mu * Z1 + math.sqrt(s) * Z2; p = sig(Q); s1 = p * (1 - p); s2 = s1 * (1 - 2 * p); s3 = s1 * (1 - 6 * p + 6 * p * p)
    return ((W * s1).sum(), (W * Z1 * (p - PY1)).sum(), (W * (p * p - 2 * p * PY1 + PY1)).sum(),
            (W * Z1 * s2).sum(), (W * s3).sum() / 2, (W * Z1 ** 2 * s1).sum())
def Dfun(lam_, mu, s):
    Vh, A, R2, Vm, Vs, EZ2s1 = mom(mu, s); a_ = A - mu * Vh
    Am = EZ2s1 - Vh - mu * Vm; As = Vm / 2 - mu * Vs
    G = 1 / (lam_ + Vh * S); T1 = (nu * G).sum() / rho ** 2; T2 = (nu * S * G ** 2).sum() / rho ** 2
    T3 = N * (om * S ** 2 * G ** 2).sum(); T4 = (nu * S ** 2 * G ** 3).sum() / rho ** 2
    J = np.array([[1 + Am * T1 - a_ * T2 * Vm, As * T1 - a_ * T2 * Vs],
                  [2 * mu - 2 * a_ * Am * T2 + 2 * a_ * a_ * T4 * Vm, 1 - 2 * a_ * As * T2 + 2 * a_ * a_ * T4 * Vs]])
    return R2 * T3 * (J[0, 0] * Vh / 2 - J[0, 1] * A) / np.linalg.det(J)
mu0 = brentq(lambda m_: mom(m_, 0.0)[1], 1e-3, 50.0, xtol=1e-15)
Vh, A, R2, Vm, Vs, A_mu = mom(mu0, 0.0)
Ew, Varw = quad["Ew"], quad["Varw"]
m1 = -mu0 * Ew / A_mu; cc = mu0 ** 2 * Varw / Vh ** 2
E2 = mu0 ** 2 * (Ew ** 2 / A_mu + Varw / Vh)
h = 1e-6; Dp = (Dfun(h, mu0 + m1 * h, cc * h * h) - Dfun(-h, mu0 - m1 * h, cc * h * h)) / (2 * h)
print(f"limit measure: rho {rho:.6f} mu0 {mu0:.6f} Vh {Vh:.6f} R2/Vh {R2 / Vh:.6f} A_mu {A_mu:.6f}; D(0) {Dfun(0.0, mu0, 0.0):.6e} "
      f"(N R2/(2 Vh) {N * R2 / (2 * Vh):.6e}); E0''(0) {E2:.6e}; D'(0) {Dp:.6e}")
print(f"k_inf on the limiting spectrum = {-Dp / (d * E2):.5f}", flush=True)
