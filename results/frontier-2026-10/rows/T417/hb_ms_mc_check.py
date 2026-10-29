"""T417 audit of hb_ms_radius.py's noise term (agent A, 18 Oct 2026): iterate the exact second-moment map and a direct
Monte Carlo of heavy ball on Gaussian x (batch B), and compare E|e_t|^2 after t steps."""
import numpy as np
h = np.array([1.0, 0.3, 0.05]); d = len(h); rng = np.random.default_rng(417)
for eta, beta, B in ((0.3, 0.5, 1), (0.15, 0.8, 2), (0.5, 0.2, 4)):
    e0 = np.ones(d); T = 30
    a = e0 ** 2; x = a.copy(); c = a.copy()          # start e_0 = e_{-1}
    for _ in range(T):
        kb = 1 + beta - eta * h
        a2 = kb ** 2 * a + eta ** 2 / B * (h ** 2 * a + (h @ a) * h) - 2 * beta * kb * x + beta ** 2 * c
        x, c, a = kb * a - beta * x, a, a2
    R = 400_000; E = np.tile(e0, (R, 1)); Ep = E.copy()
    for _ in range(T):
        X = rng.standard_normal((R, B, d)) * np.sqrt(h)
        g = np.einsum('rbi,rbj,rj->ri', X, X, E) / B
        E, Ep = E - eta * g + beta * (E - Ep), E
    m = (E ** 2).sum(1); print(f"eta {eta} beta {beta} B {B}: map {a.sum():.5f}  MC {m.mean():.5f} +- {m.std() / np.sqrt(R):.5f}")
