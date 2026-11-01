"""T262 vs the T244 limit (agent A, 18 Oct): phi_L = n theta_L -> 3 pi / (t A_t), A_t = (1/t) int_0^t exp(s + sqrt2 W_s) ds.
Monte Carlo of the Brownian functional; prints quantiles 10/25/50/75/90 and mean/sd of log phi, to compare with two_input_run1.txt."""
import numpy as np
rng = np.random.default_rng(0); R = 200000; ds = 1e-3
for t in (0.25, 0.5, 1.0, 2.0):
    m = int(round(t / ds)); W = np.zeros(R); I = np.zeros(R)
    for k in range(m):
        s = k * ds; e0 = np.exp(s + np.sqrt(2) * W)
        W += np.sqrt(ds) * rng.standard_normal(R)
        I += 0.5 * ds * (e0 + np.exp(s + ds + np.sqrt(2) * W))
    phi = 3 * np.pi / I; lp = np.log(phi)
    print(f't {t}: quantiles', np.round(np.quantile(phi, [.1, .25, .5, .75, .9]), 2), f' mean log {lp.mean():.2f}  sd log {lp.std():.2f}', flush=True)
