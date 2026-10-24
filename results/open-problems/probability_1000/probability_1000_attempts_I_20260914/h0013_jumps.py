"""H0013/H0014: the growth of the Hardy quantity, computed from the jumps alone.

The grid computation in h0013_hardy.py verified, to three decimals at two independent points, that at a
downward jump of size m at x,

    log B(x) = m - 2 log(delta x^{delta-1}) + O(1).

That formula lets the asymptotics be read off the jump process alone, which is all that matters here:
a symmetric alpha-stable process has Levy measure nu(|z| > m) = c m^{-alpha}, so the number of downward
jumps in [1, X] of size at least (2 delta - 2) log x + t is about
  int_1^X (c/2) ((2 delta - 2) log x + t)^{-alpha} dx  ->  infinity  for every fixed t,
since the requirement grows only logarithmically while the jump measure decays polynomially in the
threshold.  Hence lim sup_x log B(x) = +infinity a.s., which forces lambda_ess = 0 and noncompactness
for EVERY delta > 0 - not only for delta <= 1/alpha, which is the range the paper's Proposition 5.2
covers.  This script simulates the jumps directly and prints the running maximum.
"""
import numpy as np, sys
from math import log, exp

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
delta = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
X = float(sys.argv[3]) if len(sys.argv) > 3 else 1e6
c = float(sys.argv[4]) if len(sys.argv) > 4 else 0.124     # calibrated to the CMS path in h0013_hardy.py
rng = np.random.default_rng(5)

# downward jumps of size >= m0 form a Poisson process on [1,X] with rate (c/2) m0^{-alpha}
m0 = 1.0
rate = (c / 2) * m0 ** (-alpha)
N = rng.poisson(rate * X)
pos = np.sort(rng.random(N) * X)
sizes = m0 * rng.random(N) ** (-1 / alpha)          # Pareto(alpha) tail above m0
pos = pos[pos >= 1.0]; sizes = sizes[-len(pos):] if len(pos) else sizes
val = sizes - 2 * np.log(delta * pos ** (delta - 1))
print(f"alpha={alpha} delta={delta} X={X:g}  {len(pos)} downward jumps of size >= {m0}")
print(f"{'x <=':>10} {'max log B so far':>17} {'at x':>12} {'jump':>9} {'2log(delta x^(d-1))':>21}")
run = -np.inf
for cut in (3e2, 1e3, 1e4, 1e5, 1e6, X):
    if cut > X: continue
    sel = pos <= cut
    if not sel.any(): continue
    i = int(np.argmax(np.where(sel, val, -np.inf)))
    print(f"{cut:>10.0f} {val[i]:>17.2f} {pos[i]:>12.1f} {sizes[i]:>9.2f} {2*log(delta*pos[i]**(delta-1)):>21.2f}")
# how many jumps clear the bar, by decade
print("\njumps that clear the bar (log B > 0), by decade of x:")
for lo, hi in ((1, 1e2), (1e2, 1e3), (1e3, 1e4), (1e4, 1e5), (1e5, 1e6)):
    if lo > X: break
    s = (pos >= lo) & (pos < min(hi, X)) & (val > 0)
    print(f"  [{lo:g}, {min(hi,X):g}): {int(s.sum())}")
