"""T417 (agent A, 18 Oct 2026): the matching lower bound, by an explicit heavy-ball choice.
delta = min(2/sqrt(kappa), 4 c B h_min/tr H),  sqrt(beta) = 1 - delta/2,  eta = delta^2/(4 h_min)   (critical damping at h_min;
eta h_max <= 1; effective step eta/(1-beta) ~ delta/(4 h_min) <= c B/tr H). Reports min over random points of (1 - rho_HB)/delta, and
the resulting speedup against the SGD ceiling 1 - rho_SGD <= 4 h_min min(B/tr H, 1/h_max) (Jensen + S<1 at beta = 0).
usage: hb_speedup_lower_check.py trials c"""
import sys, numpy as np
from hb_ms_secular import full
rng = np.random.default_rng(4171); T = int(sys.argv[1]); c = float(sys.argv[2]); worst = np.inf; wS = np.inf; unstable = 0
for t in range(T):
    d = int(rng.integers(2, 30)); h = np.sort(10 ** rng.uniform(-3, 0, d))[::-1]; B = int(10 ** rng.uniform(0, 4))
    tr, hmax, hmin = h.sum(), h[0], h[-1]; kap = hmax / hmin
    delta = min(2 / np.sqrt(kap), 4 * c * B * hmin / tr); beta = (1 - delta / 2) ** 2; eta = delta ** 2 / (4 * hmin)
    r = max(abs(np.linalg.eigvals(full(h, eta, beta, B))))
    if r >= 1: unstable += 1; continue
    worst = min(worst, (1 - r) / delta)
    target = min(max(1.0, B * hmax / tr), np.sqrt(kap))
    wS = min(wS, (1 - r) / (4 * hmin * min(B / tr, 1 / hmax)) / target)
print(f"c={c}: unstable {unstable}/{T}; min (1-rho_HB)/delta = {worst:.4f}; min speedup lower bound / min(max(1,B h_max/trH),sqrt kappa) = {wS:.4f}")
