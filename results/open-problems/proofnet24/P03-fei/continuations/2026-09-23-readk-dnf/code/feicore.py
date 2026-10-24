"""Core spectral quantities for FEI experiments.

Truth tables are int8/float arrays of length 2^n, entry x = f(x) in {+1,-1},
bit i of x is coordinate i.  Fourier: fhat(S) = 2^-n sum_x f(x) (-1)^{|x&S|}.
Entropy in bits.
"""
import numpy as np
import numba as nb

LOG2 = np.log(2.0)


def polite(cores=(14, 15)):
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        if cores:
            p.cpu_affinity(list(cores))
    except Exception:
        pass


def wht(v):
    """Unnormalised Walsh-Hadamard transform (float64), returns new array."""
    a = np.array(v, dtype=np.float64).copy()
    n = a.size.bit_length() - 1
    h = 1
    for _ in range(n):
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy()
        y = a[:, 1, :]
        a[:, 0, :] = x + y
        a[:, 1, :] = x - y
        a = a.reshape(-1)
        h *= 2
    return a


def spectrum(tt):
    tt = np.asarray(tt, dtype=np.float64)
    N = tt.size
    c = wht(tt) / N
    return c * c  # P(S)


def popcounts(n):
    N = 1 << n
    pc = np.zeros(N, dtype=np.int64)
    for i in range(n):
        pc += (np.arange(N) >> i) & 1
    return pc


def entropy(P):
    P = P[P > 0]
    return float(-(P * np.log2(P)).sum())


def influences(P, n):
    idx = np.arange(P.size)
    return np.array([P[(idx >> i) & 1 == 1].sum() for i in range(n)])


def total_influence(P, n):
    return float((P * popcounts(n)).sum())


def zeta_subset(P):
    """g(A) = sum_{S subset of A} P(S)."""
    g = np.array(P, dtype=np.float64).copy()
    N = g.size
    n = N.bit_length() - 1
    for i in range(n):
        g = g.reshape(-1, 2, 1 << i)
        g[:, 1, :] += g[:, 0, :]
        g = g.reshape(-1)
    return g


def hit_prob(P):
    """beta(B) = Pr[S cap B != empty] for every block B (indexed by mask)."""
    N = P.size
    g = zeta_subset(P)
    full = N - 1
    comp = full ^ np.arange(N)
    return 1.0 - g[comp]


@nb.njit(cache=True)
def min_tree_cost(beta, n):
    """cost[B] = sum over internal nodes of the best binary tree on B of beta(node).
    Leaves cost 0.  Returns (cost array, best split array)."""
    N = 1 << n
    cost = np.full(N, np.inf)
    split = np.zeros(N, dtype=np.int64)
    cost[0] = 0.0
    for B in range(1, N):
        if B & (B - 1) == 0:
            cost[B] = 0.0
            continue
        low = B & (-B)
        rest = B ^ low
        best = np.inf
        bs = 0
        # B1 = low | sub, sub a proper submask of rest (sub != rest)
        sub = rest
        while True:
            sub = (sub - 1) & rest
            B1 = low | sub
            c = cost[B1] + cost[B ^ B1]
            if c < best:
                best = c
                bs = B1
            if sub == 0:
                break
        cost[B] = beta[B] + best
        split[B] = bs
    return cost, split


def tree_of(split, B):
    if B & (B - 1) == 0:
        return int(B).bit_length() - 1
    B1 = int(split[B])
    return (tree_of(split, B1), tree_of(split, B ^ B1))


def summary(tt, n, tree=False):
    P = spectrum(tt)
    H = entropy(P)
    I = total_influence(P, n)
    beta = hit_prob(P)
    cost, split = min_tree_cost(beta, n)
    full = (1 << n) - 1
    out = dict(n=n, H=H, I=I, HI=H / I if I > 0 else 0.0,
               HC=cost[full] / I if I > 0 else 0.0)
    if tree:
        out['tree'] = tree_of(split, full)
    return out


# ---------------- families -----------------

def tt_from_func(n, fn):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)
    return np.array([fn(b) for b in bits], dtype=np.int8)


def majority(n):
    xs = np.arange(1 << n)
    pc = popcounts(n)
    return np.where(2 * pc > n, -1, 1).astype(np.int8)


def and_n(n):
    t = np.ones(1 << n, dtype=np.int8)
    t[-1] = -1
    return t


def tribes(w, s):
    n = w * s
    xs = np.arange(1 << n)
    val = np.zeros(1 << n, dtype=bool)
    for t in range(s):
        m = ((1 << w) - 1) << (t * w)
        val |= (xs & m) == m
    return np.where(val, -1, 1).astype(np.int8)


def recmaj3(d):
    n = 3 ** d
    xs = np.arange(1 << n)
    vals = ((xs[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)
    while vals.shape[1] > 1:
        v = vals.reshape(vals.shape[0], -1, 3).sum(axis=2)
        vals = (v >= 2).astype(np.int8)
    return np.where(vals[:, 0] == 1, -1, 1).astype(np.int8)


def bent(m):
    """inner product on m (even) variables."""
    n = m
    xs = np.arange(1 << n)
    s = np.zeros(1 << n, dtype=np.int64)
    for k in range(m // 2):
        s += ((xs >> (2 * k)) & 1) * ((xs >> (2 * k + 1)) & 1)
    return np.where(s % 2 == 1, -1, 1).astype(np.int8)


def addressing(k):
    n = k + (1 << k)
    xs = np.arange(1 << n)
    a = xs & ((1 << k) - 1)
    bit = (xs >> (k + a)) & 1
    return np.where(bit == 1, -1, 1).astype(np.int8)


def compose(g, gn, inner):
    """g on gn inputs; inner = list of (tt, n_i) blocks; returns tt of g(inner...)."""
    ns = [k for _, k in inner]
    n = sum(ns)
    xs = np.arange(1 << n)
    outbits = np.zeros(1 << n, dtype=np.int64)
    off = 0
    for j, (t, k) in enumerate(inner):
        sub = (xs >> off) & ((1 << k) - 1)
        vj = (np.asarray(t)[sub] == -1).astype(np.int64)
        outbits |= vj << j
        off += k
    return np.asarray(g)[outbits].astype(np.int8), n
