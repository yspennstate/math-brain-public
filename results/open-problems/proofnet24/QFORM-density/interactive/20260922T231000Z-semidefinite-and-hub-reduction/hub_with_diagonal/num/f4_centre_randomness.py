try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Theorem 2.5 prediction: in the aligned family Q = a Xh^2 + 2 Xh t + sigma t^2 + lam V^2 + eps Y (Y an extra independent
# uniform coordinate; only two large eigenvalues), the log(1/D_H) growth is cut off by the level-1 randomness of the
# centre C' = eps Y: max density ~ const + coef * min(log(1/D_H), (1/2) log(1/eps) + ...).
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(41)
m = 30
wv = np.ones(m)/np.sqrt(m)
N = 250000
fh = uniform_law()
a = 0.2; lam = -1.0
t0 = time.time()
for DH in [0.1, 0.003]:
    sigma = (1 - DH)/a
    for eps in [0.0, 1e-3, 1e-2, 1e-1, 1.0]:
        def samp(r):
            L = r.random((N, m)) @ wv - 0.5*np.sqrt(m)
            V = r.random((N, m)) @ wv - 0.5*np.sqrt(m)
            Y = r.random(N) - 0.5
            return L, sigma*L*L + lam*V*V + eps*Y
        sg = np.unique(np.concatenate([np.linspace(-0.3, 0.3, 25), np.linspace(-0.02, 0.02, 9)]))
        d = density_on_grid(a, 0.0, samp, fh, sg, 2, rng)
        j = int(np.argmax(d))
        print("D_H %.3f eps %.0e : max_s p_Q = %.3f at s = %.3f  t=%.0fs" % (DH, eps, d[j], sg[j], time.time()-t0), flush=True)
