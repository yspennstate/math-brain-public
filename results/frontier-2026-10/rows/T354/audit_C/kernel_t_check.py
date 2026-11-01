"""Check (2/sqrt pi) int_0^inf (1 - eps sqrt(pi) t erfcx(eps t)) e^(-t^2 v) dt = 1/(sqrt(v)+eps) with the solver's own nodes."""
import math
import numpy as np
from scipy.special import erfcx
for Nt in (160, 240):
    tn, tw = np.polynomial.legendre.leggauss(Nt)
    t = (tn + 1) * 6.5 / 2
    for eps in (0.0, 1.0, 3.0, 10.0):
        w = tw * 6.5 / 2 * 2 / math.sqrt(math.pi) * (1 - eps * math.sqrt(math.pi) * t * erfcx(eps * t))
        err = max(abs(np.dot(w, np.exp(-t * t * v)) * (math.sqrt(v) + eps) - 1) for v in (1.0, 4.8, 10.0, 81.0))
        print("nodes %d eps %g max rel err %.2e" % (Nt, eps, err))
