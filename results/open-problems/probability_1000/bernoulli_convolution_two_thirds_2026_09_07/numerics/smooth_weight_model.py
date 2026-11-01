"""Is the zero mean of the kernel the SOURCE of the cancellation, or only its leading annihilation?

On the consecutive block 1 <= m <= 2^(K+1)-1 the digit algorithm gives c(m) = 2^(-#nonzero digits).
The kernel in the paper's variable u = m/2^K is g(u) = (3/(pi u)) cos(pi u) sin(pi u / 3), int g = 0.

If the vanishing integral were the mechanism, replacing c by a locally SMOOTH model of itself would
reproduce the signed sum.  Test: smooth c over a window of w consecutive m and compare
    sum c(m) g(m/2^K)      against      sum cbar_w(m) g(m/2^K).
The residual sum (c - cbar) g is the part carried by the fine correlation of c with the kernel.
"""
import numpy as np

g = lambda u: (3.0 / (np.pi * u)) * np.cos(np.pi * u) * np.sin(np.pi * u / 3.0)

def digit_weight(K, M):
    """c(m) for m = 1..M by the forced digit algorithm: at each level the residue mod 3 forces the digit."""
    m = np.arange(1, M + 1, dtype=object)
    nz = np.zeros(M, dtype=np.int64)
    cur = np.array([int(x) for x in m], dtype=np.int64)
    for i in range(K, -1, -1):
        # top term is eps_K 2^K 3^0 at i=K ... use the recursion u_{j-1} = (2/3)(u_j - e_j) in integers:
        # here work with nu = sum eps_i 2^i 3^(K-i); mod 3 only i=K survives: eps_K 2^K = nu (mod 3)
        pass
    # direct: build the map by enumeration on the block instead (exact, no algebra risk)
    return None

def block_weights(K):
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    B = 2 ** (K + 1) - 1
    sel = (nu >= 1) & (nu <= B)
    m, cm = nu[sel], c[sel]
    o = np.argsort(m)
    return m[o].astype(float), cm[o]

print(f"{'K':>3} {'w':>5} {'sum c g':>12} {'sum cbar g':>12} {'smooth share':>14} {'sum |c g|':>12}")
for K in (8, 10, 12):
    m, c = block_weights(K)
    u = m / (2.0 ** K)
    gu = g(u)
    raw = float((c * gu).sum())
    absraw = float((c * np.abs(gu)).sum())
    for w in (16, 64, 256):
        k = np.ones(w) / w
        cbar = np.convolve(c, k, mode="same")
        sm = float((cbar * gu).sum())
        print(f"{K:>3} {w:>5} {raw:>12.6f} {sm:>12.6f} {100*sm/raw:>13.1f}% {absraw:>12.4f}")
    print()
