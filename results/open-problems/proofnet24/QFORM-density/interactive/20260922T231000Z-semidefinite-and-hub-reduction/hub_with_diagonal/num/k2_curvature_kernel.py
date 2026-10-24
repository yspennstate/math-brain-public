try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Exact check of (I1): for h(tau) quadratic with leading coefficient sigma (modulus) and critical value h_c,
# int_{interval of length 2} |h|^{-1/2} <= |sigma|^{-1/2}(5.66 + 1.42 log_+(|sigma|/|h_c|)),  worst case over the
# position of the interval (sup over interval placement = bathtub with the measure capped at 2).
import numpy as np
rng = np.random.default_rng(3)
def meas(eps, sig, hc):
    # |{tau : |sig tau^2 + hc| < eps}|  (critical point at 0), no interval restriction
    A = (-hc - eps)/sig; B = (-hc + eps)/sig
    lo, hi = np.minimum(A, B), np.maximum(A, B)
    return 2*(np.sqrt(np.maximum(hi, 0)) - np.sqrt(np.maximum(lo, 0)))
worst = 0.0; rec = None
for trial in range(600):
    sig = rng.choice([-1, 1])*10**rng.uniform(-3, 3)
    hc = rng.choice([-1, 1])*10**rng.uniform(-8, 3)
    lam = np.geomspace(1e-9, 1e14, 60001)
    m = np.minimum(2.0, meas(lam**-2.0, sig, hc))
    val = np.trapezoid(m, lam) if hasattr(np, 'trapezoid') else np.trapz(m, lam)
    bound = abs(sig)**-0.5*(5.66 + 1.42*max(0.0, np.log(abs(sig)/abs(hc))))
    r = val/bound
    if r > worst:
        worst, rec = r, (sig, hc, val, bound)
print("worst ratio (exact bathtub value)/(I1 bound) =", round(worst, 4), "at (sigma, h_c, value, bound) =", rec, flush=True)
