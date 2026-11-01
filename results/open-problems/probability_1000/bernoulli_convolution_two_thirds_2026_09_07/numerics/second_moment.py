"""The variance of Err(k0)/L over window positions is bounded by an absolute constant.

Err(k0) = sum_{eps != 0} c_eps D_{k0}(nu_eps),  D_{k0}(nu) = e(k0 nu/P) G(nu),
G(nu) = sum_{j<L} e(j nu/P).  Averaging k0 over Z_P kills every nu != 0, so E[Err] = 0 exactly.
For the second moment, distinct eps give distinct nu with |nu| <= 3^(K+1) - 2^(K+1) < P, so
nu_eps = nu_eps' mod P forces eps = eps' unless the difference is exactly +-P.  Ignoring those,

    Var(Err) = sum_{eps != 0} c_eps^2 |G(nu_eps)|^2.

Now sum_eps c_eps^2 = prod_i (1 + 2*(1/4)) = (3/2)^(K+1) EXACTLY, and |G|^2 averages to L over a
full period, so heuristically Var(Err) ~ (3/2)^(K+1) L and

    Var(Err/L) ~ (3/2)^(K+1) / L = (3/2)^(K+1) / (3/2)^K = 3/2,

an absolute constant.  If that holds, Chebyshev bounds the density of positions with Err > C L by
(3/2)/C^2 -- which is exactly the stable quantile structure that was measured.
"""
import numpy as np

print(f"{'K':>3} {'L':>6} {'Var(Err/L) direct':>18} {'sum c^2|G|^2 / L^2':>20} {'(3/2)^(K+1)/L':>15}")
for K in (6, 8, 10, 12, 14):
    P = 3 ** (K + 1)
    L = max(1, int(round(1.5 ** K)))

    # direct: every window sum over one period
    k = np.arange(P, dtype=np.float64)
    F = np.ones(P)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    del k
    Fd = np.concatenate((F, F[:L])); del F
    pre = np.concatenate(([0.0], np.cumsum(Fd))); del Fd
    ws = pre[L:L + P] - pre[0:P]; del pre
    err = ((2.0 ** (K + 1)) * ws - L) / L; del ws
    var_direct = float(err.var()); del err

    # the character-side formula
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    nz = nu != 0
    v, cc = nu[nz].astype(float), c[nz]
    s = np.sin(np.pi * v / P)
    G2 = np.where(np.abs(s) < 1e-14, float(L) ** 2, (np.sin(np.pi * L * v / P) / s) ** 2)
    formula = float((cc ** 2 * G2).sum()) / L ** 2
    print(f"{K:>3} {L:>6} {var_direct:>18.6f} {formula:>20.6f} {(1.5 ** (K + 1)) / L:>15.6f}")
