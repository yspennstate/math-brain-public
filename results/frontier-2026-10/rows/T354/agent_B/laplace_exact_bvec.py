# Second audit of agent B's iid remainder lemma (T354): x*/x0 by an exact route with no Monte Carlo.
# y^(-1/2) = pi^(-1/2) int_0^inf s^(-1/2) e^(-s y) ds and, under iid sampling, the lags of v_k factorize:
#   E[g_{k-i} v_k^(-1/2)] = pi^(-1/2) int s^(-1/2) E[g e^(-s c_i g^2)] prod_{j != i} M(s c_j) ds,  c_j = d beta2^j,
# M(u) = E e^(-u g^2). D(x) = (1-b1) sum_i b1^i (that). The product is summed exactly while u = s c_j gmax^2 > 1e-2 and by
# the cumulant series of log M to order 5 beyond (geometric tails in closed form). s = w^2 on a Gauss-Legendre grid.
# Model: the NOTE's test model, g_i = x + b_i, b = (9, -1 x 9), f'(x) = x. Argv: beta2 beta1 [nodes].
import sys, math, numpy as np
from scipy.optimize import brentq
b2 = float(sys.argv[1]); b1 = float(sys.argv[2]); N = int(sys.argv[3]) if len(sys.argv) > 3 else 300
d = 1 - b2; import os; B = np.array([float(t) for t in os.environ["BVEC"].split(",")])
K = (1 - b1) / (1 - b1 * b2); x0 = d * K * np.mean(B**3) / (2 * np.mean(B**2))
W = 7.0
wn, ww = np.polynomial.legendre.leggauss(N); w = (wn + 1) * W / 2; ww = ww * W / 2; s = w * w
I = 0 if b1 == 0 else int(np.ceil(np.log(1e-15) / np.log(b1)))
def D(x):
    g = x + B; g2 = g * g; gmax = g2.max()
    mu = [np.mean(g2 ** k) for k in range(1, 6)]   # raw moments -> cumulants of g^2
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
        # tail j >= J0: sum_j log M(u_j) = sum_k (-1)^k kap_k/k! sum_j u_j^k
        for k in range(1, 6):
            tail = (sv * d) ** k * b2 ** (k * J0) / (1 - b2 ** k)
            L[a] += (-1) ** k * kap[k-1] / math.factorial(k) * tail
    tot = 0.0
    for i in range(I + 1):
        u = s * d * b2 ** i
        E = np.exp(-np.outer(u, g2))
        num = (E * g).mean(axis=1); Mi = E.mean(axis=1)
        val = (ww * 2 * num / Mi * np.exp(L)).sum() / np.sqrt(np.pi)
        tot += (1 - b1) * b1 ** i * val
    return tot
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-14 * x0)
print("beta2 %s beta1 %s nodes %d: x*/x0 = %.9f   (D(0.5x0) %.3e, D(2x0) %.3e)" % (sys.argv[1], sys.argv[2], N, xs / x0, D(0.5*x0), D(2*x0)))
