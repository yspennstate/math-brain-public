"""Check of the composition step in FLOW 12(u), fact 3.

F(x, z) = f(x, phi(z_1), ..., phi(z_k)) with f the hidden-coordinate function of mono_hidden.py and phi = MAJ_m on
m fresh variables per block. Claim: Inf_x and E_x are the same for F as for f, exactly; the block variables have
influence below... (printed). Usage: python mono_hidden_comp.py K M   (n = K*M + 1 must be <= 24 or so)
"""
import sys
import numpy as np
from mono_hidden import wht, erasure


def build(k, m):
    n = k * m + 1
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    x = (idx >> (k * m)) & 1
    ys = []
    for j in range(k):
        s = np.zeros(N, dtype=np.int64)
        for t in range(m):
            s += (idx >> (j * m + t)) & 1
        ys.append(s >= (m + 1) // 2)
    wt = np.zeros(N, dtype=np.int64)
    for y in ys:
        wt += y
    maj = wt >= (k + 1) // 2
    ge = np.ones(N, dtype=bool)
    for j in range((k - 1) // 2):
        ge &= ys[j]
    eq = ge.copy()
    for j in range((k - 1) // 2, k):
        eq &= ~ys[j]
    f = maj | ((x == 1) & ge)
    return n, np.where(f, -1.0, 1.0)


def main():
    k, m = int(sys.argv[1]), int(sys.argv[2])
    n, f = build(k, m)
    mu = wht(f) ** 2
    er = erasure(mu, n)
    xi = k * m
    print("k=%d m=%d n=%d  x: Inf=%.6e E/Inf=%.6f | block var 0: Inf=%.4e E/Inf=%.4f | last block var: Inf=%.4e E/Inf=%.4f | max other Inf=%.4e" % (
        k, m, n, er[xi][0], er[xi][1] / er[xi][0], er[0][0], er[0][1] / er[0][0],
        er[xi - 1][0], er[xi - 1][1] / er[xi - 1][0], max(a for a, _ in er[:xi])), flush=True)


if __name__ == "__main__":
    main()
