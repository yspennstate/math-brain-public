"""Core routines for the W3-05 noise-semigroup study of FEI.

Conventions.  f is a numpy array of length 2^n with entries +1/-1; bit i of the index x is coordinate i,
and bit value 1 means x_i = -1.  Then chi_S(x) = (-1)^{popcount(S & x)} and
fhat(S) = 2^{-n} sum_x f(x) chi_S(x).  w(S) = fhat(S)^2 is the spectral sample.

All entropies in this module are in NATS unless a name ends in _bits.
"""
import math
import numpy as np

LN2 = math.log(2.0)


def lowprio():
    """Apply the machine rules: below-normal priority, restricted cores."""
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
    except Exception as exc:  # pragma: no cover
        print("lowprio failed:", exc)


def wht(f):
    """Normalized Walsh-Hadamard transform, float64."""
    a = np.array(f, dtype=np.float64).copy()
    n = a.size.bit_length() - 1
    h = 1
    N = a.size
    while h < N:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy()
        y = a[:, 1, :]
        a[:, 0, :] = x + y
        a[:, 1, :] = x - y
        a = a.reshape(N)
        h *= 2
    return a / N


def popcounts(n):
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    pc = np.zeros(N, dtype=np.int64)
    for i in range(n):
        pc += (idx >> i) & 1
    return pc


class Spec:
    """Spectral data of a Boolean function given by its weight vector w (length 2^n)."""

    def __init__(self, w, n, tol=1e-300):
        self.n = n
        self.w = np.asarray(w, dtype=np.float64)
        self.size = popcounts(n)
        self.mask = self.w > tol
        self.ws = self.w[self.mask]
        self.ks = self.size[self.mask].astype(np.float64)
        self.L = np.log(1.0 / self.ws)          # log(1/w(S)) on the support
        self.idx = np.nonzero(self.mask)[0]

    @classmethod
    def from_table(cls, f):
        f = np.asarray(f)
        n = f.size.bit_length() - 1
        a = wht(f)
        return cls(a * a, n)

    # --- basic functionals -------------------------------------------------
    def H(self):
        return float(np.sum(self.ws * self.L))

    def I(self):
        return float(np.sum(self.ws * self.ks))

    def influences(self):
        n = self.n
        inf = np.zeros(n)
        for i in range(n):
            sel = ((self.idx >> i) & 1) == 1
            inf[i] = self.ws[sel].sum()
        return inf

    def levels(self):
        """W^k and within-level entropies h_k (nats)."""
        n = self.n
        W = np.zeros(n + 1)
        h = np.zeros(n + 1)
        for k in range(n + 1):
            sel = self.ks == k
            Wk = self.ws[sel].sum()
            W[k] = Wk
            if Wk > 0:
                p = self.ws[sel] / Wk
                p = p[p > 0]
                h[k] = float(-(p * np.log(p)).sum())
        return W, h

    # --- the tilted spectral law q_t -------------------------------------------
    def tilt(self, t):
        """Return dict with Z_t, E_t|S|, Var_t|S|, H(q_t), dH/dt, and the unnormalized G(t)."""
        e = -2.0 * t * self.ks
        m = e.max()
        u = self.ws * np.exp(e - m)          # proportional to q_t
        Zs = u.sum()
        q = u / Zs
        logZ = math.log(Zs) + m              # log Z_t
        Ek = float((q * self.ks).sum())
        Vk = float((q * (self.ks - Ek) ** 2).sum())
        logq = np.log(q, where=q > 0, out=np.full_like(q, -np.inf))
        qpos = q > 0
        Hq = float(-(q[qpos] * logq[qpos]).sum())
        # -dH/dt = 2 Cov_q(|S|, -log q)
        mlq = np.where(qpos, -logq, 0.0)
        Em = float((q * mlq).sum())
        cov = float((q * (self.ks - Ek) * (mlq - Em)).sum())
        return dict(t=t, logZ=logZ, Ek=Ek, Vk=Vk, H=Hq, mdHdt=2.0 * cov)

    # --- KKL split -----------------------------------------------------------------
    def kkl_split(self):
        """H = K + R with K = sum_S (w/|S|) sum_{i in S} log(1/Inf_i),
        R = sum_S w log(G_S / w), G_S the geometric mean influence over S (nats).
        The empty set contributes w(0) log(1/w(0)) to R by convention (G_empty := 1)."""
        inf = self.influences()
        n = self.n
        with np.errstate(divide='ignore'):
            li = np.where(inf > 0, np.log(1.0 / np.maximum(inf, 1e-300)), 0.0)
        s = np.zeros(self.ws.size)
        for i in range(n):
            s += li[i] * ((self.idx >> i) & 1)
        nz = self.ks > 0
        K = float(np.sum(self.ws[nz] * s[nz] / self.ks[nz]))
        H = self.H()
        return K, H - K, inf


def table_from_func(n, fn):
    """Build a +-1 table from a python predicate fn(bits) -> +1/-1 where bits[i] in {0,1} (1 = x_i=-1)."""
    N = 1 << n
    out = np.empty(N, dtype=np.int8)
    for x in range(N):
        bits = [(x >> i) & 1 for i in range(n)]
        out[x] = fn(bits)
    return out


# ---------------------------------------------------------------- families
def majority(n):
    pc = popcounts(n)
    # bit 1 means x_i = -1 ("true"); majority of the +-1 values: f = -1 iff more than half are -1
    return np.where(pc > n // 2, -1, 1).astype(np.int8)


def tribes(width, count):
    n = width * count
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    out = np.ones(N, dtype=np.int8)
    anytribe = np.zeros(N, dtype=bool)
    full = (1 << width) - 1
    for j in range(count):
        anytribe |= ((idx >> (j * width)) & full) == full
    out[anytribe] = -1
    return out


def inner_product(m):
    """Bent function IP on 2m variables: f = (-1)^{sum x_i y_i} with bits."""
    n = 2 * m
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    par = np.zeros(N, dtype=np.int64)
    for i in range(m):
        par ^= ((idx >> i) & 1) & ((idx >> (i + m)) & 1)
    return np.where(par == 1, -1, 1).astype(np.int8)


def dictator(n, i=0):
    idx = np.arange(1 << n, dtype=np.int64)
    return np.where((idx >> i) & 1, -1, 1).astype(np.int8)


def parity(n, S=None):
    idx = np.arange(1 << n, dtype=np.int64)
    par = np.zeros(1 << n, dtype=np.int64)
    for i in (range(n) if S is None else S):
        par ^= (idx >> i) & 1
    return np.where(par == 1, -1, 1).astype(np.int8)


def flip(f, points):
    g = np.array(f, dtype=np.int8).copy()
    for x in points:
        g[x] = -g[x]
    return g


def addressing(a):
    """Addressing function: a address bits, 2^a data bits; n = a + 2^a."""
    n = a + (1 << a)
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    addr = idx & ((1 << a) - 1)
    bit = (idx >> (a + addr)) & 1
    return np.where(bit == 1, -1, 1).astype(np.int8)


def load_numaro():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(here, '..', '..', 'inputs', 'numaro18_pm1_table.npy')
    return np.load(p)
