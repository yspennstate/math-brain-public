# Second route for the T249 crossover: the posted ordered-phase law is lambda_perp ~ kappa * k * L chi_1^L with kappa = q* + beta T*/chi_1,
# T* = q*/(1-chi_1), and k the Koenigs value lim delta_l / chi_1^l of the correlation map. Claim: as eps = 1-chi_1 -> 0,
# k(delta_0) = eps delta_0 / (eps + beta delta_0 / 2) (1 + o(1)) -> 2 eps / beta, so kappa * k -> 2 q*, which is the t -> infinity end 2 q* L e^-t.
import numpy as np, sys
N = 120; z, w = np.polynomial.hermite_e.hermegauss(N); w = w / w.sum()
phi = np.tanh; dphi = lambda x: 1 / np.cosh(x) ** 2; ddphi = lambda x: -2 * np.tanh(x) / np.cosh(x) ** 2
def qstar(sw2, sb2):
    q = 1.0
    for _ in range(20000):
        qn = sw2 * (w * phi(np.sqrt(q) * z) ** 2).sum() + sb2
        if abs(qn - q) < 1e-15: break
        q = qn
    return q
def chi1(sw2, sb2):
    q = qstar(sw2, sb2); return sw2 * (w * dphi(np.sqrt(q) * z) ** 2).sum(), q
def solve_sw2(eps, sb2):
    lo, hi = 0.5, 3.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if chi1(mid, sb2)[0] < 1 - eps: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
sb2 = 0.05
print("eps beta | delta0: k*beta/(2 eps) measured, predicted 1/(1 + 2 eps/(beta delta0)) | kappa*k/(2 q*) measured")
for eps in (0.02, 0.01, 0.005):
    sw2 = solve_sw2(eps, sb2); c1, q = chi1(sw2, sb2)
    beta = sw2 * q * (w * ddphi(np.sqrt(q) * z) ** 2).sum()
    d0 = np.array([1.5, 1.0, 0.5, 0.2, 0.05]); c = 1 - d0; u = np.sqrt(q) * z; W = w[None, :, None] * w[None, None, :]
    L = int(round(14 / eps))
    for l in range(L):
        v = np.sqrt(q) * (c[:, None, None] * z[None, :, None] + np.sqrt(np.clip(1 - c ** 2, 0, None))[:, None, None] * z[None, None, :])
        c = (sw2 * (W * phi(u)[None, :, None] * phi(v)).sum((1, 2)) + sb2) / q
    k = (1 - c) / c1 ** L; kappa = q + beta * (q / (1 - c1)) / c1
    for a, b in zip(d0, k):
        print("%.3f %.4f | %.2f: %.4f %.4f | %.4f" % (eps, beta, a, b * beta / (2 * eps), 1 / (1 + 2 * eps / (beta * a)), kappa * b / (2 * q)))
    sys.stdout.flush()
