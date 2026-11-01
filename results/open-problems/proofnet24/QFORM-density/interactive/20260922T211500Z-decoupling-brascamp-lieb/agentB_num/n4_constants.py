try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from scipy.integrate import quad
# C_H: int_0^inf min(1, phi(v^-2)) dv with phi(u) = 2u(9.34 + log_+(1/u))  (indefinite S, D_S >= 1)
phi = lambda u: 2*u*(9.34 + max(0.0, np.log(1/u)))
f = lambda v: min(1.0, phi(v**-2))
CH_indef = quad(f, 0, 50, limit=500)[0] + quad(f, 50, np.inf, limit=500)[0]
CH_def = 2*np.sqrt(2*np.pi)
print("C_H indefinite:", CH_indef, " definite:", CH_def)
print("route (i), |a_ii|>=0.3:", max(CH_indef, CH_def)/np.sqrt(0.3))
# route (ii): D >= 0.365 ; p <= D^{-1/2}(5.2 + log_+(16 sqrtD) + E log_+(1/|s-kappa|)), E log_+ <= 2 log_+(alpha1)+2, alpha1 <= 2 sqrt2
for D in (0.365, 0.5, 1, 4, 100):
    val = (5.2 + max(0, np.log(16*np.sqrt(D))) + 2*np.log(2*np.sqrt(2)) + 2)/np.sqrt(D)
    print(f"route (ii) D={D}: {val:.3f}   definite: {np.pi/np.sqrt(D):.3f}")
# check: E log_+(M/|Z|) for Z = sigma(X-x0)^2 + h with X uniform, worst case h
sig = 1.0; M = 1.0
xs = np.linspace(-0.5, 0.5, 2000001)
worst = 0
for h in np.linspace(-0.3, 0.3, 61):
    Z = np.abs(sig*xs**2 + h); v = np.mean(np.maximum(0, np.log(M/np.maximum(Z, 1e-300))))
    worst = max(worst, v)
print("E log_+(1/|X^2+h|) worst over h (uniform X):", worst, " bound log_+(8M/sig)+2 =", np.log(8)+2)
