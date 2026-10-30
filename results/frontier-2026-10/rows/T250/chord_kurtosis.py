"""T250 (agent A, 18 Oct): the uniformity mechanism for lemma (ii). With d = relu(y) - relu(x), y = cos(t) x + sin(t) w, print
kappa(t) = E d^4 / (E d^2)^2 (per coordinate) and E d^2 / t^2 on (0, pi/2], by 2-D Gauss-Hermite quadrature split at the kinks.
A bounded kappa on the whole interval is what makes the relative fluctuation of |d|^2 O(1/sqrt n) uniformly in t."""
import numpy as np
from scipy import integrate
def mom(t, p):
    f = lambda w, x: (max(np.cos(t) * x + np.sin(t) * w, 0) - max(x, 0)) ** p * np.exp(-(x * x + w * w) / 2) / (2 * np.pi)
    v, _ = integrate.dblquad(f, -9, 9, -9, 9, epsabs=1e-13, epsrel=1e-9); return v
for t in [1e-3, 1e-2, 0.05, 0.2, 0.5, 1.0, np.pi / 2]:
    m2, m4 = mom(t, 2), mom(t, 4)
    print(f"t {t:7.4f}: E d^2/t^2 {m2 / t**2:.5f}  kappa {m4 / m2**2:.4f}", flush=True)
