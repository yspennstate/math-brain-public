# T354: c(s) at eps >= 0 (agent B, 20 Oct 2026). Same continuum limit as c_closed.py (beta1 = 0, a_i = 1, n -> infinity at
# fixed s = n d); psi(y) = (sq + eps)/(sq sqrt(y) + eps), sq = sqrt(B2), has Taylor coefficients p1 = -r/2, p2/2, p3/6 at 1 in place
# of -1/2, 3/8, -5/16, and the eta moments do not depend on eps, so
#   c(s) = r K - (p2/2) r1 avg Q - p2 r2 cb/(r K) - p3 r1 avg[k Q]/(r K),   x0 = r d K B3/(2 B2).
# Argv: eps, then values of s. Optional env B="6,2,-1" P="0.1,0.1,0.8" for another b.
import sys, os, numpy as np
from scipy.integrate import quad
b = np.array([float(v) for v in os.environ.get("B", "9,-1").split(",")])
p = np.array([float(v) for v in os.environ.get("P", "0.1,0.9").split(",")])
B2 = p @ b**2; B3 = p @ b**3; Z = b**2 - B2; r1 = (p @ Z**2) / B2**2; r2 = (p @ (b * Z**2)) / (B2 * B3)
eps = float(sys.argv[1]); sq = np.sqrt(B2); r = sq / (sq + eps)
p2 = sq * (eps + 3 * sq) / (4 * (eps + sq)**2); p3 = -3 * sq * (eps**2 + 4 * eps * sq + 5 * sq**2) / (8 * (eps + sq)**3)
def c_of(s):
    q = np.tanh(s / 2)
    k = lambda t: 1 - (1 - np.exp(-t)) / s
    Q = lambda t: 0.5 - (1 - np.exp(-t))**2 / s - np.exp(-2*t) * q / s
    cbf = lambda t: 1 - 2*(1 - np.exp(-t))/s - (1 - np.exp(-2*t))/(2*s) + 2*(1 - np.exp(-t))**2/s**2
    av = lambda f: quad(f, 0, s, limit=200)[0] / s
    K = av(k); Qb = av(Q); cb = av(cbf); kQ = av(lambda t: k(t) * Q(t))
    return r*K - p2/2*r1*Qb - p2*r2*cb/(r*K) - p3*r1*kQ/(r*K)
print("b", b, "p", p, "r1 %.4f r2 %.4f eps %g r %.4f p2 %.5f p3 %.5f" % (r1, r2, eps, r, p2, p3))
print("  limits: c(0+) = r/2 - p2 r2/(3r) = %.4f   c(inf) = r - p2 r1/4 - p2 r2/r - p3 r1/(2r) = %.4f"
      % (r/2 - p2*r2/(3*r), r - p2*r1/4 - p2*r2/r - p3*r1/(2*r)))
for a in sys.argv[2:]:
    print("  s %g  c %.4f" % (float(a), c_of(float(a))))
