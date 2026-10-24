"""numba versions of the biased transform of g and of (Htilde, It, p_out); same conventions as gate.py."""
import math
import numpy as np
import numba as nb
from gate import load_table, N

TAB = load_table()


@nb.njit(cache=True)
def btransform(tab, p):
    n = p.shape[0]
    a = tab.copy()
    L = a.shape[0]
    for i in range(n):
        pi = p[i]
        q = 1.0 - pi
        s = math.sqrt(pi * q)
        step = 1 << i
        for base in range(0, L, 2 * step):
            for k in range(base, base + step):
                lo = a[k]; hi = a[k + step]
                a[k] = q * lo + pi * hi
                a[k + step] = s * (lo - hi)
    return a


@nb.njit(cache=True)
def stats(c, n):
    L = c.shape[0]
    It = np.zeros(n)
    Ht = 0.0
    for x in range(L):
        w = c[x] * c[x]
        if w > 0.0:
            Ht -= w * math.log2(w)
            y = x
            i = 0
            while y:
                if y & 1:
                    It[i] += w
                y >>= 1
                i += 1
    return Ht, It


def evaluate(p, tab=TAB):
    p = np.asarray(p, dtype=np.float64)
    c = btransform(tab, p)
    Ht, It = stats(c, N)
    return Ht, It, 0.5 * (1.0 - c[0]), c


if __name__ == "__main__":
    import time
    from gate import evaluate as slow_eval
    rng = np.random.default_rng(3)
    for k in range(3):
        p = rng.uniform(0.05, 0.95, N)
        a = slow_eval(TAB, p); b = evaluate(p)
        print("check: dHt %.1e dIt %.1e dpout %.1e" % (abs(a[0] - b[0]), np.abs(a[1] - b[1]).max(), abs(a[2] - b[2])))
    t0 = time.time()
    for k in range(20):
        evaluate(p)
    print("fast eval %.4f s" % ((time.time() - t0) / 20))


@nb.njit(cache=True)
def grad_parts(c, a, mu):
    """t1[j] = sum_{T not ni j} c_T c_{T u j} Psi_T, t2[j] = sum_{T ni j} w_T Psi_T, Psi_T = omega_T + log2 w_T + 1/ln2."""
    n = a.shape[0]
    L = c.shape[0]
    inv_ln2 = 1.0 / math.log(2.0)
    Psi = np.zeros(L)
    for x in range(L):
        w = c[x] * c[x]
        if w > 0.0:
            om = 0.0
            y = x; i = 0
            while y:
                if y & 1:
                    om += a[i]
                y >>= 1; i += 1
            Psi[x] = om + math.log2(w) + inv_ln2
    t1 = np.zeros(n); t2 = np.zeros(n)
    for j in range(n):
        b = 1 << j
        s1 = 0.0; s2 = 0.0
        for x in range(L):
            if x & b:
                s2 += c[x] * c[x] * Psi[x]
            else:
                s1 += c[x] * Psi[x] * c[x | b]
        t1[j] = s1; t2[j] = s2
    return t1, t2
