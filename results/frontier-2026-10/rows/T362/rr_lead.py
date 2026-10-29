"""T362 (agent A, 18 Oct): checks for the leading-term proof on the rr_mixed instance (l = 0).
(1) phi(r) = m / (g G*/2), m the stationary epoch-end mean, is <= 1 on r in [0,1) for n1 <= 200 (proved in DOSSIER; this is the check).
(2) optimal-step last-iterate error against G*^2 ln^2 T / (8 mu T^2) for X0 = +1 and -1 (the transient and the bias can cancel)."""
import os, sys, numpy as np
sys.argv = ['x', 'run', '10', '1000000']                     # makes rr_mixed's main block skip every instance (n1 = 0)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import rr_mixed as R
worst = 0.0
for n1 in (1, 2, 3, 5, 10, 50, 200):
    for r in np.linspace(0, 0.999999, 4001):
        q = np.arange(n1); S = np.sum(r ** q)
        worst = max(worst, 2 * np.sum(r ** q - r ** n1) / ((n1 + 1) * (1 - r) * S))
print("(1) max phi over n1 <= 200, r in [0,1):", worst, flush=True)
for (n, n1) in ((100, 10), (100, 50), (1000, 100)):
    L, l, s = 1.0, 0.0, 1.0; mu = n1 * L / n
    for K in (1000, 10000):
        T = n * K; gs = np.exp(np.linspace(np.log(0.05 * np.log(T) / (mu * T)), np.log(20 * np.log(T) / (mu * T)), 3000))
        EA, EB, EA2, EAB, EB2 = R.epoch_moments_vec(gs, n, n1, L, l, s)
        for X0 in (1.0, -1.0):
            m1 = np.full_like(gs, X0); m2 = m1 * m1
            for _ in range(K): m1, m2 = EA * m1 + EB, EA2 * m2 + 2 * EAB * m1 + EB2
            e = 0.5 * mu * m2; i = int(e.argmin()); ref = s * s * np.log(T) ** 2 / (8 * mu * T * T)
            print(f"(2) n {n} n1 {n1} K {K} X0 {X0:+.0f}: best {e[i]:.4e}  g mu T / ln T {gs[i] * mu * T / np.log(T):.3f}  "
                  f"best / (G*^2 ln^2 T / (8 mu T^2)) {e[i] / ref:.4f}", flush=True)
