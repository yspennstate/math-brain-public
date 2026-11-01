"""B(f) = sum_i H(S_i | S_{-i}) / I(f)  -- the erasure entropy of the spectral sample
over the total influence.

Why it matters: min_i (a_i/b_i) <= (sum a_i)/(sum b_i), so a bound sum_i Delta_i H <= K I
gives rho_0 <= K and hence FEI. Delta_i H = JS_i + H(S_i | S_{-i}) exactly, and the P03
record's erasure reduction says sum_i H(S_i|S_{-i}) <= K I alone implies FEI with K + 2/ln2.
Erasure entropy is at most the entropy, so this target is WEAKER than FEI - which is what
makes it a route. The crude bound H(S_i|S_{-i}) <= h(Inf_i) is useless (h(x)/x -> infinity),
so everything depends on how much the conditioning saves. That is what this measures."""
import numpy as np, itertools, sys
from math import log2

def spectrum(f, n):
    """f: 0/1 truth table of length 2^n -> mu(S) = fhat(S)^2"""
    a = 1.0 - 2.0*f.astype(np.float64)      # true = -1
    N = 1 << n
    step = 1
    while step < N:
        a = a.reshape(-1, 2, step)
        u = a[:, 0, :].copy(); v = a[:, 1, :].copy()
        a[:, 0, :] = u + v; a[:, 1, :] = u - v
        a = a.reshape(-1)
        step *= 2
    a /= N
    return a*a

def h2v(x):
    out = np.zeros_like(x)
    m = (x > 0) & (x < 1)
    out[m] = -x[m]*np.log2(x[m]) - (1-x[m])*np.log2(1-x[m])
    return out

def stats(mu, n):
    """returns I, H, B = sum_i H(S_i | S_{-i})"""
    H = 0.0
    nz = mu > 0
    H = float(-(mu[nz]*np.log2(mu[nz])).sum())
    idx = np.arange(len(mu))
    popc = np.array([bin(k).count('1') for k in idx]) if n <= 22 else None
    I = float((mu*popc).sum())
    B = 0.0
    m3 = mu.reshape([2]*n) if n <= 22 else None
    for i in range(n):
        # split on bit i (bit i of the index)
        bit = (idx >> i) & 1
        mu0 = mu[bit == 0]; mu1 = mu[bit == 1]
        s = mu0 + mu1
        with np.errstate(divide='ignore', invalid='ignore'):
            r = np.where(s > 0, mu1/np.maximum(s, 1e-300), 0.0)
        B += float((s*h2v(r)).sum())
    return I, H, B

def tribes(s, w):
    """AND of s ORs of w fresh variables, as a truth table on n = s*w bits"""
    n = s*w
    idx = np.arange(1 << n, dtype=np.int64)
    out = np.ones(1 << n, dtype=np.int8)
    for b in range(s):
        block = (idx >> (b*w)) & ((1 << w) - 1)
        out &= (block != 0).astype(np.int8)      # OR of the block
    return out, n

if __name__ == '__main__':
    print("family                        n     I        H      H/I     B      B/I")
    for (s, w) in [(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),
                   (2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(2,4),(3,4),(4,4),(5,4),(3,5),(4,5)]:
        n = s*w
        if n > 22: continue
        f, n = tribes(s, w)
        mu = spectrum(f, n)
        I, H, B = stats(mu, n)
        print("tribes s=%-2d w=%-2d            %-5d %7.4f %7.4f %6.3f %7.4f %6.3f"
              % (s, w, n, I, H, H/I, B, B/I))
        sys.stdout.flush()
