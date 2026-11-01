"""Growth check for the extremal hub configuration: pure star + rank one, Q = 2 X_h L + V^2, uniform laws, n1 leaves,
w, v random orthonormal (spread).  E1 exact (delta = 0) on a fine s-grid around 0 with 1e6 samples, plus the exact
window estimator (delta = .002) as a spike-free companion; the Gaussian limit is 3.6207 at s = 0."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from lib import *
Ns = int(sys.argv[1]); n1s = [int(x) for x in sys.argv[2].split(',')]
fh = U(); t0 = time.time()
sv = np.linspace(-0.02, 0.04, 31)
for n1 in n1s:
    rng = np.random.default_rng(100 + n1)
    B, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = B.T
    tot = np.zeros(len(sv)); tot2 = np.zeros(len(sv)); win = np.zeros(len(sv)); done = 0
    while done < Ns:
        m = min(50000, Ns - done)
        Xp = rng.uniform(-0.5, 0.5, (m, n1))
        T = Xp @ w; V = Xp @ v; R = V*V
        e = hub_cond_values(0.0, T, R, sv, fh)
        tot += e.sum(0); tot2 += (e*e).sum(0)
        win += hub_window_values(0.0, T, R, sv, fh, 0.002).sum(0)/(2*0.002)
        done += m
    mean = tot/Ns; se = np.sqrt(np.maximum(tot2/Ns - mean**2, 0)/Ns); win /= Ns
    j = int(np.argmax(mean)); k = int(np.argmax(win))
    print(f"n1={n1:5d}: E1 exact max {mean[j]:.4f} +- {se[j]:.4f} at s={sv[j]:+.3f};  p(0) = {mean[10]:.4f} +- {se[10]:.4f};  "
          f"window(.002) max {win[k]:.4f} at s={sv[k]:+.3f}   t={time.time()-t0:.0f}", flush=True)
print("Gaussian limit p(0) = 3.6207", flush=True)
