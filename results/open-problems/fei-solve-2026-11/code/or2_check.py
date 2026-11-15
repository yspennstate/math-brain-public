"""D_i/Inf_i = (E_i + J_i)/Inf_i for OR of k disjoint 2-clauses; which k gives 5.7825 (FLOW 12(y), FEIB27)?"""
import numpy as np


def wht(v):
    v = v.astype(float).copy(); h = 1; N = len(v)
    while h < N:
        v = v.reshape(-1, 2 * h); a = v[:, :h].copy(); b = v[:, h:].copy()
        v[:, :h] = a + b; v[:, h:] = a - b; v = v.reshape(N); h *= 2
    return v / N


def H(f):
    p = wht(f) ** 2; p = p[p > 1e-300]
    return float(-(p * np.log2(p)).sum())


for k in range(2, 10):
    n = 2 * k; x = np.arange(1 << n)
    bits = lambda i: (x >> i) & 1
    f = np.where(np.any([bits(2 * j) & bits(2 * j + 1) for j in range(k)], axis=0), -1.0, 1.0)
    i = 0
    f1 = f[bits(i) == 0]; f0 = f[bits(i) == 1]
    D = H(f) - 0.5 * H(f1) - 0.5 * H(f0)
    inf = float(np.mean(f1 != f0))
    print(f"k={k}: D_0/Inf_0 = {D / inf:.4f}  Inf_0={inf:.5f}  H/I={H(f) / (n * inf):.4f}")
