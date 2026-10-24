"""Family (b) at the cusp s ~ 0 with E2 (E1 and the window scan are biased low at a cusp: E1 has a heavy right tail,
the window averages over +-delta).  Q = a X_h^2 + 2 X_h L + lam V^2, n1 = 100 uniform leaves."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from lib import *
N = int(sys.argv[1]); t0 = time.time()
n1 = 100; rng = np.random.default_rng(7)
B, _ = np.linalg.qr(rng.normal(size=(n1, 6))); w, v = B.T[:2]
sv = [-0.003, 0.0, 0.001, 0.003, 0.006, 0.012]
for a in (0.0, 0.01, 0.03, 0.1, 0.3):
    A = np.zeros((n1+1, n1+1)); A[0, 0] = a; A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] = np.outer(v, v)
    m, se = fibre_density_v(A, [U()]*(n1+1), sv, N=N, rng=np.random.default_rng(11))
    m3 = mu3(A)
    print(f"a={a:.2f} lam=+1 mu3={m3:.3f}: p(s) at {sv} = {np.round(m,3)} +- {np.round(se,3)}   F=mu3*max={m3*m.max():.3f}  t={time.time()-t0:.0f}", flush=True)
