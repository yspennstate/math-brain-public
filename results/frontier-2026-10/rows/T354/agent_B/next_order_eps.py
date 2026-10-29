# T354 iid, eps >= 0: next-order term of the vanishing-step limit point, formula and an exact check (agent B, 20 Oct 2026).
# m/(sqrt(v) + eps) = (m/(s+eps)) psi(y), psi(y) = (s+eps)/(s sqrt(y) + eps), s = sqrt(V). With p1, p2, p3 the derivatives of psi at 1,
#   p1 = -r/2, p2 = s(eps+3s)/(4(eps+s)^2), p3 = -3s(eps^2+4 eps s+5 s^2)/(8(eps+s)^3), r = s/(s+eps),
# the same O(d^2) bookkeeping as next_order.py gives x0 = r d K B3/(2 B2) and
#   x*/x0 = 1 + d [ r K - (p2/4) S/B2^2 - (p2/r)(K2/K) E[b Z^2]/(B2 B3) - (p3/(2r)) S/B2^2 ] + O(d^2)
# (eps = 0: p2 = 3/4, p3 = -15/8, r = 1, the eps = 0 bracket).
# EXACT CHECK: 1/(sqrt(v) + eps) = int_0^inf k(u) e^(-u v) du with k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt(u))]
# (write 1/(a+eps) = int e^(-t(a+eps)) dt and e^(-t sqrt(v)) = int t/(2 sqrt(pi)) u^(-3/2) e^(-t^2/(4u)) e^(-u v) du, then do the t
# integral). Under iid sampling e^(-u v) factorizes over lags, so the second audit's solver (laplace_exact.py) carries over with
# its u^(-1/2) weight multiplied by the bracket. Argv: eps beta2 beta1 [nodes]; env BVEC (default the test model).
import sys, os, math, numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx
eps = float(sys.argv[1]); b2 = float(sys.argv[2]); b1 = float(sys.argv[3]); N = int(sys.argv[4]) if len(sys.argv) > 4 else 300
B = np.array([float(t) for t in os.environ.get("BVEC", "9" + ",-1" * 9).split(",")])
d = 1 - b2; B2 = np.mean(B**2); B3 = np.mean(B**3); Z = B**2 - B2; S = np.mean(Z**2); EbZ2 = np.mean(B * Z**2); s0 = math.sqrt(B2)
K = (1 - b1) / (1 - b1 * b2); K2 = (1 - b1) / (1 - b1 * b2 * b2); r = s0 / (s0 + eps)
p2 = s0 * (eps + 3 * s0) / (4 * (eps + s0) ** 2); p3 = -3 * s0 * (eps**2 + 4 * eps * s0 + 5 * s0**2) / (8 * (eps + s0) ** 3)
br = r * K - p2 / 4 * S / B2**2 - p2 / r * K2 / K * EbZ2 / (B2 * B3) - p3 / (2 * r) * S / B2**2
x0 = r * d * K * B3 / (2 * B2)
W = 7.0
wn, ww = np.polynomial.legendre.leggauss(N); w = (wn + 1) * W / 2; ww = ww * W / 2; s = w * w
hk = 1 - eps * math.sqrt(math.pi) * w * erfcx(eps * w)          # k(u) / (pi u)^(-1/2) at u = w^2
I = 0 if b1 == 0 else int(np.ceil(np.log(1e-15) / np.log(b1)))
def D(x):
    g = x + B; g2 = g * g; gmax = g2.max()
    mu = [np.mean(g2 ** k) for k in range(1, 6)]
    k1 = mu[0]; k2 = mu[1] - mu[0]**2
    k3 = mu[2] - 3*mu[1]*mu[0] + 2*mu[0]**3
    k4 = mu[3] - 4*mu[2]*mu[0] - 3*mu[1]**2 + 12*mu[1]*mu[0]**2 - 6*mu[0]**4
    k5 = mu[4] - 5*mu[3]*mu[0] - 10*mu[2]*mu[1] + 20*mu[2]*mu[0]**2 + 30*mu[1]**2*mu[0] - 60*mu[1]*mu[0]**3 + 24*mu[0]**5
    kap = [k1, k2, k3, k4, k5]
    L = np.zeros_like(s)
    for a, sv in enumerate(s):
        J0 = int(np.ceil(np.log(1e-2 / (sv * d * gmax)) / np.log(b2))) if sv * d * gmax > 1e-2 else 0
        J0 = max(J0, 0)
        if J0 > 0:
            u = sv * d * b2 ** np.arange(J0)
            L[a] = np.log(np.mean(np.exp(-np.outer(u, g2)), axis=1)).sum()
        for k in range(1, 6):
            L[a] += (-1) ** k * kap[k-1] / math.factorial(k) * (sv * d) ** k * b2 ** (k * J0) / (1 - b2 ** k)
    tot = 0.0
    for i in range(I + 1):
        u = s * d * b2 ** i
        E = np.exp(-np.outer(u, g2))
        num = (E * g).mean(axis=1); Mi = E.mean(axis=1)
        tot += (1 - b1) * b1 ** i * (ww * 2 * hk * num / Mi * np.exp(L)).sum() / np.sqrt(np.pi)
    return tot
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-14 * x0)
print("eps %s beta2 %s beta1 %s nodes %d: exact x*/x0 = %.9f  (x*-x0)/(d x0) exact %.5f predicted %.5f" % (sys.argv[1], sys.argv[2], sys.argv[3], N, xs / x0, (xs / x0 - 1) / d, br))
