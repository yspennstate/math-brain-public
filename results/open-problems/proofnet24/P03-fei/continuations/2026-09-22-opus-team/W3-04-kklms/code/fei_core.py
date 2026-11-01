"""Core spectral quantities for the W3-04 (KKLMS) group.

Conventions: F is a +-1 truth table of length 2^n, bit i of the index x is coordinate i,
-1 means "true".  Fhat(S) = 2^-n sum_x F(x) chi_S(x), H = sum Fhat^2 log2(1/Fhat^2),
I = sum |S| Fhat^2.  lambda(S) = log2(1/Fhat(S)^2)/|S| is the per-element log-coefficient;
mu is the size-biased spectral law mu(S) = |S| Fhat(S)^2 / I.  Identity used throughout:
H - Fhat(0)^2 log2(1/Fhat(0)^2) = int_0^inf T(C) dC with T(C) = sum_{S: lambda(S) >= C} |S| Fhat(S)^2.
"""
import numpy as np


def limit_process():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
    except Exception as e:  # pragma: no cover
        print("psutil limit failed:", e)


def walsh(F):
    """Exact Walsh-Hadamard transform of an integer table; returns integer array 2^n * Fhat."""
    a = np.array(F, dtype=np.int64).copy()
    h = 1
    N = a.size
    while h < N:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(-1)
        h *= 2
    return a


def popcounts(n):
    idx = np.arange(1 << n, dtype=np.int64)
    pc = np.zeros(1 << n, dtype=np.int64)
    for i in range(n):
        pc += (idx >> i) & 1
    return pc


def spectrum(F):
    """Return (n, p, sizes) with p[S] = Fhat(S)^2 (float64) and sizes[S] = |S|."""
    N = len(F)
    n = N.bit_length() - 1
    w = walsh(F)
    p = (w.astype(np.float64) / N) ** 2
    return n, p, popcounts(n)


def entropy_bits(p):
    q = p[p > 0]
    return float(-(q * np.log2(q)).sum())


def HI(F):
    n, p, sz = spectrum(F)
    return entropy_bits(p), float((sz * p).sum())


# ----------------------------------------------------------------- families
def table_from_func(n, fn):
    idx = np.arange(1 << n, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(n)) & 1).astype(np.int8)  # 1 = true
    return fn(bits)


def pm(b):
    """boolean array (True = true) -> +-1 with -1 = true"""
    return np.where(b, -1, 1).astype(np.int8)


def majority(n):
    return table_from_func(n, lambda B: pm(B.sum(1) > n // 2))


def tribes(w, s):
    def fn(B):
        t = np.zeros(B.shape[0], dtype=bool)
        for j in range(s):
            t |= B[:, j * w:(j + 1) * w].all(1)
        return pm(t)
    return table_from_func(w * s, fn)


def recmaj3(depth):
    n = 3 ** depth

    def fn(B):
        cur = B.astype(np.int8)
        while cur.shape[1] > 1:
            cur = (cur.reshape(cur.shape[0], -1, 3).sum(2) >= 2).astype(np.int8)
        return pm(cur[:, 0] == 1)
    return table_from_func(n, fn)


def bent_plus_flip(m):
    """inner-product bent function on m (even) variables plus a flip variable z (last coordinate):
    F(y,z) = b(y) for z false, b(y)(1 - 2[y = all true]) for z true (F4 convention)."""
    n = m + 1

    def fn(B):
        y = B[:, :m]
        ip = np.zeros(B.shape[0], dtype=np.int8)
        for i in range(0, m, 2):
            ip ^= (y[:, i] & y[:, i + 1]).astype(np.int8)
        val = ip.astype(bool)
        flip = B[:, m].astype(bool) & (y.sum(1) == m)
        return pm(val ^ flip)
    return table_from_func(n, fn)


def ltf(w, theta):
    w = np.asarray(w, dtype=np.float64)
    n = len(w)
    return table_from_func(n, lambda B: pm((B * 2 - 1) @ w - theta > 0))


def and_n(n):
    return table_from_func(n, lambda B: pm(B.all(1)))


def one_point_flip(n):
    """Majority_{n-1} (n-1 odd) plus a flip of one point y* on coordinate z (F4 Prop 6.1 family)."""
    m = n - 1

    def fn(B):
        y = B[:, :m]
        maj = y.sum(1) > m // 2
        ystar = np.zeros(m, dtype=np.int8)
        ystar[: (m - 1) // 2] = 1
        at = (y == ystar).all(1)
        return pm(maj | (B[:, m].astype(bool) & at))
    return table_from_func(n, fn)


def numaro_g():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "..", "inputs", "numaro18_pm1_table.npy")
    return np.load(path).astype(np.int8)


def lam_mu_arrays(F):
    """lambda(S) and mu(S) over nonempty S with Fhat != 0."""
    n, p, sz = spectrum(F)
    mask = (p > 0) & (sz > 0)
    I = float((sz * p).sum())
    lam = np.log2(1.0 / p[mask]) / sz[mask]
    mu = sz[mask] * p[mask] / I
    return lam, mu, p[mask], sz[mask], I


def tail_T(lam, mu, Cs):
    """T(C)/I = mu(lambda >= C)."""
    order = np.argsort(lam)
    ls, ms = lam[order], mu[order]
    cum = np.cumsum(ms[::-1])[::-1]
    out = []
    for C in Cs:
        k = np.searchsorted(ls, C, side="left")
        out.append(float(cum[k]) if k < len(ls) else 0.0)
    return out
