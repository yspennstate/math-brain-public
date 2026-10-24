"""Float scan of the block function used in the chain theorem.

Phi_K(s) = 2 E(s) + sum_{k<K} 2^-k psi(T^k s),   s in [1/2, 1),
E(s) = sum_{l>=0} 2^l eps(2^-l s),  psi(u) = eps(2 d(u)).
If Phi_K >= 0 on [1/2,1) then every AND/OR chain satisfies H <= 4 I (block induction, see REPORT).
"""
import numpy as np
import numba as nb
from chains_defect3 import eps, D_I


@nb.njit(cache=True)
def E_of(s):
    acc = 0.0
    for l in range(90):
        acc += (2.0 ** l) * eps(s * 2.0 ** (-l))
    return acc


@nb.njit(cache=True)
def Phi(s, K):
    acc = 2.0 * E_of(s)
    u = s
    w = 1.0
    for k in range(K):
        d = min(u, 1.0 - u)
        acc += w * eps(2.0 * d)
        u = (2.0 * u) % 1.0
        w *= 0.5
    return acc


@nb.njit(cache=True)
def scan(ss, K):
    out = np.empty(ss.shape[0])
    for i in range(ss.shape[0]):
        out[i] = Phi(ss[i], K)
    return out


if __name__ == "__main__":
    s = 0.5 + np.arange(0, 2 ** 20) / 2.0 ** 21     # dyadic grid of [1/2,1), step 2^-21
    for K in [2, 3, 4, 5, 6, 8, 10, 14, 20, 40]:
        v = scan(s, K)
        k = int(np.argmin(v))
        print("K=%2d  min Phi_K on grid = %.8f at s = %.8f ; fraction of grid below 0: %.3e" % (K, v[k], s[k], np.mean(v < 0)))
    t = np.arange(1, 2 ** 20) / 2.0 ** 20
    D = np.array([D_I(x, 60)[0] for x in t])
    print("max D on the dyadic grid of step 2^-20: %.10f at t = %.8f" % (D.max(), t[np.argmax(D)]))
    # Lipschitz estimate of Phi_6 on the grid
    v6 = scan(s, 6)
    print("max |Phi_6(s+h) - Phi_6(s)|/h on grid (h = 2^-21): %.3f" % (np.max(np.abs(np.diff(v6))) * 2.0 ** 21))
