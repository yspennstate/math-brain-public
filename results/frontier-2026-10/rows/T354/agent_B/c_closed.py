# T354: c(s) = lim (x*/x0 - 1)/d at fixed s = n d, n -> infinity (beta1 = 0, eps = 0, a_i = 1), as theta-averages of the
# continuum lag sums (agent B, 20 Oct 2026). theta = p d in [0, s) is the position in the epoch; lag tau = j d has weight e^-tau.
# c = K - (3/8) Qbar - (3/4) cb E[bZ^2]/(K B2 B3) + (15/8) avg[k Q]/K, with
#   k(t) = 1 - (1 - e^-t)/s                                   (K = avg k: the reshuffling factor)
#   Q(t) = (z2/V^2) [1/2 - (1 - e^-t)^2/s - e^-2t q/s],  q = tanh(s/2)   (E eta^2 / d)
#   cb  = avg [1 - 2(1 - e^-t)/s - (1 - e^-2t)/(2s) + 2(1 - e^-t)^2/s^2]  (E[b eta^2] = cb E[bZ^2] (d/V)^2)
# Argv: values of s. Model b = 9 on a tenth, -1 elsewhere.
import sys, numpy as np
from scipy.integrate import quad
p = np.array([0.1, 0.9]); b = np.array([9.0, -1.0])
B2 = p @ b**2; B3 = p @ b**3; Z = b**2 - B2; z2 = p @ Z**2; bZ2 = p @ (b * Z**2); V = B2
def c_of(s):
    q = np.tanh(s / 2)
    k = lambda t: 1 - (1 - np.exp(-t)) / s
    Q = lambda t: (z2 / V**2) * (0.5 - (1 - np.exp(-t))**2 / s - np.exp(-2*t) * q / s)
    cbf = lambda t: 1 - 2*(1 - np.exp(-t))/s - (1 - np.exp(-2*t))/(2*s) + 2*(1 - np.exp(-t))**2/s**2
    av = lambda f: quad(f, 0, s, limit=200)[0] / s
    K = av(k); Qb = av(Q); cb = av(cbf); kQ = av(lambda t: k(t) * Q(t))
    return K - 3/8*Qb - 3/4*cb*bZ2/(K*B2*B3) + 15/8*kQ/K, K
for a in sys.argv[1:]:
    s = float(a); c, K = c_of(s)
    print("s %g  K %.6f  c %.4f  (1-c) s %.3f" % (s, K, c, (1 - c) * s))
