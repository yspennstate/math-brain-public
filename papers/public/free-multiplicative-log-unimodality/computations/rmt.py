"""Random-matrix check of the log-uniform counterexample (Hasebe-Ueda-Wang Problem 4.3).

Log-eigenvalues of A^(1/2) U B U* A^(1/2), A = B = diag of mu_L quantiles, U Haar unitary, against g_L (lscan.density).
Usage: rmt.py L N trials. Writes rmt_L{L}.out.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")
import math
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lscan import density  # noqa: E402


L = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
trials = int(sys.argv[3]) if len(sys.argv) > 3 else 16
out = []


def say(s):
    print(s, flush=True)
    out.append(s)


ys, gs, mass, maxima = density(L, 0.001)
say("L = %g: density by continuation, mass %.6f, maxima at y = %s, g(0) = %.6f" % (L, mass, maxima, gs[0]))
rng = np.random.default_rng(20261011)
x = np.exp(-L + 2 * L * (np.arange(N) + 0.5) / N)          # mu_L quantiles
logs = []
for k in range(trials):
    Z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / math.sqrt(2)
    Qm, Rm = np.linalg.qr(Z)
    Qm = Qm * (np.diag(Rm) / np.abs(np.diag(Rm)))           # Haar
    M = (np.sqrt(x)[:, None] * Qm) @ (x[:, None] * Qm.conj().T) * np.sqrt(x)[None, :]
    M = (M + M.conj().T) / 2
    ev = np.linalg.eigvalsh(M)
    logs.append(np.log(ev[ev > 0]))
lg = np.concatenate(logs)
say("RMT: N = %d, %d trials, %d log-eigenvalues, range [%.3f, %.3f]" % (N, trials, lg.size, lg.min(), lg.max()))
hstep = ys[1] - ys[0]
ymax = maxima[-1] if maxima else 0.0
say("   window of |y|        RMT density   mean of g_L")
for lo, hi in [(0.0, 1.0), (1.0, 3.0), (3.0, 5.0), (max(ymax - 1, 0), ymax + 1), (8.0, 9.5)]:
    frac = np.mean((np.abs(lg) >= lo) & (np.abs(lg) < hi)) / (2 * (hi - lo))
    i0, i1 = int(round(lo / hstep)), min(int(round(hi / hstep)), len(gs) - 1)
    gavg = sum((gs[i] + gs[i + 1]) / 2 * hstep for i in range(i0, i1)) / (hi - lo)
    say("   [%.3f, %.3f)   %.5f      %.5f" % (lo, hi, frac, gavg))
# the dip: mean density on |y| < 1 against the window around the mode
c = np.mean(np.abs(lg) < 1.0) / 2
m = np.mean(np.abs(np.abs(lg) - ymax) < 1.0) / 4
say("RMT dip ratio (|y|<1 against ||y|-y_m|<1): %.4f" % (c / m))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rmt_L%g.out" % L), "w", encoding="utf-8").write(
    "\n".join(out) + "\n")
