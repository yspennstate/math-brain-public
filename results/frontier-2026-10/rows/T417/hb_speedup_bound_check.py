"""T417 (agent A, 18 Oct 2026): random checks of the two lemmas behind the speedup bound.
(A) every mean-square-stable heavy-ball setting has 1 - rho <= min(8 B h_min / tr H, 4 / sqrt(kappa));
(B) plain SGD with eta = min(B / (4 tr H), 1 / (2 h_max)) has 1 - rho >= eta h_min / 2.
rho = spectral radius of the full mean-square map (hb_ms_secular.full). usage: hb_speedup_bound_check.py trials"""
import sys, numpy as np
from hb_ms_secular import full
rng = np.random.default_rng(4170); T = int(sys.argv[1]); worstA = 0.0; worstB = np.inf; nst = 0
for t in range(T):
    d = int(rng.integers(2, 30)); h = np.sort(10 ** rng.uniform(-3, 0, d))[::-1]; B = int(10 ** rng.uniform(0, 4))
    tr, hmax, hmin = h.sum(), h[0], h[-1]; kap = hmax / hmin
    beta = 1 - 10 ** rng.uniform(-3, 0); eta = rng.uniform(0, 2 * (1 + beta) / hmax)
    r = max(abs(np.linalg.eigvals(full(h, eta, beta, B))))
    if r < 1:
        nst += 1; worstA = max(worstA, (1 - r) / min(8 * B * hmin / tr, 4 / np.sqrt(kap)))
    e = min(B / (4 * tr), 1 / (2 * hmax)); r0 = max(abs(np.linalg.eigvals(full(h, e, 0.0, B))))
    worstB = min(worstB, (1 - r0) / (e * hmin / 2))
print(f"(A) over {nst} stable HB points: max (1-rho)/bound = {worstA:.4f} (must be <= 1)")
print(f"(B) over {T} SGD points: min (1-rho)/(eta h_min/2) = {worstB:.4f} (must be >= 1)")
