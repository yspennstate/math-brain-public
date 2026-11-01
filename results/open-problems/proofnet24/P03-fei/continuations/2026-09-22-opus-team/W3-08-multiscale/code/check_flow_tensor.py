"""Controls for Theorem 2 (restriction flow) and Theorem 3 (tensorization).

Flow: D_delta(f) = int_0^T E A(f_t) dt with A(g) = sum_i Delta_i(g), P_t(J) = e^{-t|J|}(1-e^{-t})^{n-|J|},
E_x A(f_{J,x}) = |J| EH[J] - sum_{i in J} EH[J minus i]; integrated by Gauss-Legendre quadrature.
Tensor: D_delta(f.g) = D_delta(f) + D_delta(g) for f, g on disjoint variables.
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mslib import polite, restr_profile, basic, per_size_sums, size_weights
polite()
rng = np.random.default_rng(3)
worst_flow = 0.0
for trial in range(20):
    n = int(rng.integers(3, 9))
    N = 1 << n
    tt = rng.choice([-1, 1], size=N, p=[0.3, 0.7]).astype(np.int64)
    EH, HT = restr_profile(tt, n, False)
    fh, p, H, inf = basic(tt, n)
    pc = np.array([bin(J).count("1") for J in range(N)])
    Aexp = np.array([pc[J] * EH[J] - sum(EH[J & ~(1 << i)] for i in range(n) if (J >> i) & 1) for J in range(N)])
    for delta in (0.3, 0.5, 0.8):
        T = np.log(1 / delta)
        xs, ws = np.polynomial.legendre.leggauss(60)
        t = 0.5 * T * (xs + 1)
        integ = 0.0
        for tk, wk in zip(t, ws):
            q = np.exp(-tk)
            PJ = q ** pc * (1 - q) ** (n - pc)
            integ += 0.5 * T * wk * np.dot(PJ, Aexp)
        D = H - np.dot(size_weights(n, delta)[pc], EH)
        worst_flow = max(worst_flow, abs(integ - D))
print("max |int_0^T E A(f_t) dt - D_delta(f)| over 20 random functions x 3 rates:", worst_flow)
worst_t = 0.0
for trial in range(20):
    a, b = int(rng.integers(2, 6)), int(rng.integers(2, 6))
    f = rng.choice([-1, 1], size=1 << a).astype(np.int64)
    g = rng.choice([-1, 1], size=1 << b).astype(np.int64)
    x = np.arange(1 << (a + b))
    fg = (f[x & ((1 << a) - 1)] * g[x >> a]).astype(np.int64)
    def Dd(tt, n, d):
        EH, _ = restr_profile(tt, n, False)
        _, _, H, _ = basic(tt, n)
        return H - np.dot(size_weights(n, d), per_size_sums(EH, n))
    for d in (0.3, 0.5, 0.8):
        worst_t = max(worst_t, abs(Dd(fg, a + b, d) - Dd(f, a, d) - Dd(g, b, d)))
print("max |D(f.g) - D(f) - D(g)| over 20 random pairs x 3 rates:", worst_t)
