# T249 crossover, uniform form. Claim to test: for every depth L (not only L = t/eps),
#   D_L := Theta_diag - Theta_off(c0) = 2 q* chi^L S_L / (1 - chi^L)^2 * (1 + err),  S_L = sum_{j=1..L} (1 - chi^j)^2,
#   err = O((log L + 1/delta0)/L) for L <= 1/eps and O(eps log(1/eps) + eps/delta0) beyond.
# Small L: 2 q* L/3 (critical line). L = t/eps: (q*/eps) g(t). L >> 1/eps: 2 q* L chi^L (ordered phase).
import numpy as np, sys, math
N = 100; z, w = np.polynomial.hermite_e.hermegauss(N); w = w / w.sum()
ACT = sys.argv[1] if len(sys.argv) > 1 else "tanh"
if ACT == "tanh":
    phi = np.tanh; dphi = lambda x: 1.0 / np.cosh(x) ** 2
elif ACT == "erf":
    from scipy.special import erf as _erf; phi = lambda x: _erf(x); dphi = lambda x: 2.0 / math.sqrt(math.pi) * np.exp(-x ** 2)
elif ACT == "sin":
    phi = np.sin; dphi = np.cos
EPS = [float(a) for a in sys.argv[2].split(",")] if len(sys.argv) > 2 else [0.01, 0.0025, 0.000625]
sb2 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
C0 = np.array([-0.5, 0.0, 0.5, 0.9])
def qstar(sw2):
    q = 1.0
    for _ in range(200000):
        qn = sw2 * (w * phi(np.sqrt(q) * z) ** 2).sum() + sb2
        if abs(qn - q) < 1e-15: break
        q = qn
    return q
def chi1(sw2):
    q = qstar(sw2); return sw2 * (w * dphi(np.sqrt(q) * z) ** 2).sum(), q
def solve_sw2(eps):
    lo, hi = 0.5, 3.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if chi1(mid)[0] < 1 - eps: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
W = w[None, :, None] * w[None, None, :]
print("act %s sb2 %g; columns: L, L*eps, formula*eps/q*, then D_L/formula - 1 for c0 = %s" % (ACT, sb2, C0.tolist()))
for eps in EPS:
    sw2 = solve_sw2(eps); chi, q = chi1(sw2); u = np.sqrt(q) * z
    Ls = sorted(set([10, 30, 100, 300] + [int(round(t / eps)) for t in (0.3, 1, 3, 10, 20)]))
    c = C0.copy(); th_off = q * c; th_diag = q; S = 0.0
    print("eps %g sw2 %.6f q* %.6f" % (eps, sw2, q))
    for l in range(1, max(Ls) + 1):
        v = np.sqrt(q) * (c[:, None, None] * z[None, :, None] + np.sqrt(np.clip(1 - c ** 2, 0, None))[:, None, None] * z[None, None, :])
        dk = sw2 * (W * dphi(u)[None, :, None] * dphi(v)).sum((1, 2))
        c = (sw2 * (W * phi(u)[None, :, None] * phi(v)).sum((1, 2)) + sb2) / q
        th_off = q * c + dk * th_off; th_diag = q + chi * th_diag
        S += (1 - chi ** l) ** 2
        if l in Ls:
            F = 2 * q * chi ** l * S / (1 - chi ** l) ** 2
            D = th_diag - th_off
            print("%6d %7.3f %.5f | %s" % (l, l * eps, F * eps / q, " ".join("%+.4f" % x for x in (D / F - 1))))
    sys.stdout.flush()
