# T249: NTK of an infinite-width tanh net near the order-to-chaos line, double scaling eps = 1 - chi_1 -> 0, L = t/eps.
# Prediction (derived by hand, an agent 11 Nov): on n inputs of equal norm,
#   lam_perp * eps / q*  -> g(t) = [e^-t (2t-3) + 4 e^-2t - e^-3t] / (1 - e^-t)^2      (all n-1 eigenvalues on 1-perp)
#   cond(Theta_L) / n     -> h(t) = [1 - 2t e^-t - e^-2t] / [e^-t (2t-3) + 4 e^-2t - e^-3t],  h(0+) = 1/2, h ~ e^t/(2t)
import numpy as np, sys
N = 120; z, w = np.polynomial.hermite_e.hermegauss(N); w = w / w.sum()
phi = np.tanh; dphi = lambda x: 1.0 / np.cosh(x) ** 2
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
def run(eps, sb2, ts, n=8, d=5, seed=0):
    sw2 = solve_sw2(eps, sb2); c1, q = chi1(sw2, sb2)
    rng = np.random.default_rng(seed); X = rng.standard_normal((n, d)); X /= np.linalg.norm(X, axis=1, keepdims=True)
    iu = np.triu_indices(n, 1); c = ((q - sb2) * (X @ X.T)[iu] + sb2) / q
    u = np.sqrt(q) * z
    th_off = q * c; th_diag = q; out = []; Ls = [max(2, int(round(t / eps))) for t in ts]
    for l in range(2, max(Ls) + 1):
        v = np.sqrt(q) * (c[:, None, None] * z[None, :, None] + np.sqrt(np.clip(1 - c ** 2, 0, None))[:, None, None] * z[None, None, :])
        W = w[None, :, None] * w[None, None, :]
        dk = sw2 * (W * dphi(u)[None, :, None] * dphi(v)).sum((1, 2))
        c = (sw2 * (W * phi(u)[None, :, None] * phi(v)).sum((1, 2)) + sb2) / q
        th_off = q * c + dk * th_off; th_diag = q + c1 * th_diag
        if l in Ls:
            T = np.zeros((n, n)); T[iu] = th_off; T = T + T.T + th_diag * np.eye(n); ev = np.linalg.eigvalsh(T)
            t = l * eps; e = np.exp(-t); num = e * (2 * t - 3) + 4 * e ** 2 - e ** 3
            g = num / (1 - e) ** 2; h = (1 - 2 * t * e - e ** 2) / num
            out.append((eps, l, t, ev[0] * eps / q, ev[-2] * eps / q, g, ev[-1] / ev[0] / n, h))
    return sw2, q, out
sb2 = 0.05
print("eps L t | lam_min*eps/q lam_(n-1)*eps/q predicted_g | cond/n predicted_h")
for eps in (0.04, 0.02, 0.01, 0.005):
    sw2, q, out = run(eps, sb2, (0.5, 1, 2, 4, 6, 8))
    print("sw2 %.6f q* %.6f chi1 %.5f" % (sw2, q, 1 - eps))
    for r in out: print("%.3f %5d %.2f | %.5f %.5f %.5f | %.4f %.4f" % r)
    sys.stdout.flush()
