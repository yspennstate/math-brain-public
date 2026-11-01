"""T362 (agent A, 18 Oct): the epoch variance and the upper bound, against the exact DP (l = 0, n1 <= n/2).
Var B first order = g^4 L^2 s^2 n1^3 (n+1)/(12 n2) (Mann-Whitney); proved bound Var B <= g^4 L^2 s^2 [sqrt(n1^3 (n+1)/(12 n2)) + g L n1^3]^2.
Upper bound at g = Lam/(mu T), Lam = ln(X0 mu T/G*): E err <= G*^2 (Lam+2)^2/(8 mu T^2) + s^2 Lam^3 n n1 (1/2 + Lam sqrt(n1)/K)^2/(2 mu T^3)."""
import os, sys, numpy as np
sys.argv = ['x', 'run', '10', '1000000']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import rr_mixed as R
L, s, X0 = 1.0, 1.0, 1.0
for (n, n1) in ((100, 10), (100, 50), (1000, 100), (40, 3)):
    n2 = n - n1; mu = n1 * L / n
    for g in (1e-5, 1e-4, 1e-3):
        if g * L * n1 > 0.5: continue
        EA, EB, EA2, EAB, EB2 = [v[0] for v in R.epoch_moments_vec([g], n, n1, L, 0.0, s)]
        vb = EB2 - EB * EB; first = g**4 * L**2 * s**2 * n1**3 * (n + 1) / (12 * n2)
        bound = g**4 * L**2 * s**2 * (np.sqrt(n1**3 * (n + 1) / (12 * n2)) + g * L * n1**3) ** 2
        print(f"n {n} n1 {n1} g {g:.0e}: Var B exact {vb:.4e}  first-order {first:.4e} (ratio {vb / first:.4f})  bound {bound:.4e} ok {vb <= bound}  A det {abs(EA2 - EA * EA) < 1e-15}", flush=True)
    for K in (1000, 10000):
        T = n * K; Lam = np.log(X0 * mu * T / s); g = Lam / (mu * T)
        if g * L * n1 > 0.5: continue
        mom = [v[0] for v in R.epoch_moments_vec([g], n, n1, L, 0.0, s)]; e = R.err_from(mom, mu, K, X0)
        ub = s * s * (Lam + 2) ** 2 / (8 * mu * T * T) + s * s * Lam**3 * n * n1 * (0.5 + Lam * np.sqrt(n1) / K) ** 2 / (2 * mu * T**3)
        print(f"   K {K}: g = Lam/(mu T): exact err {e:.4e}  upper bound {ub:.4e}  ok {e <= ub}  ratio {e / ub:.3f}", flush=True)
