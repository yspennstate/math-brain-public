"""Shared routines for the W2-B extensions of the threshold-function FEI argument.

Conventions (same as F5). Index x in [0, 2^n); bit i of x equal to 1 means x_i = -1.
chi_S(x) = (-1)^{popcount(S & x)}.  fhat(S) = 2^{-n} sum_x f(x) chi_S(x).  H in bits.
sgn(t) = +1 for t > 0 and -1 for t <= 0.

Units.  A unit partition assigns every coordinate a unit id (blocks of a block-separable
function; singletons for threshold functions).  For an ordering of the units, the rank of a
coordinate is the rank of its unit.
"""
import numpy as np

try:
    from scipy.optimize import linear_sum_assignment
except Exception:  # pragma: no cover
    linear_sum_assignment = None


def setup_process():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 14, 15])
    except Exception:
        pass


# ----------------------------------------------------------------------------- basics

def popcount32(a):
    a = a.astype(np.uint32)
    a = a - ((a >> 1) & np.uint32(0x55555555))
    a = (a & np.uint32(0x33333333)) + ((a >> 2) & np.uint32(0x33333333))
    a = (a + (a >> 4)) & np.uint32(0x0F0F0F0F)
    return ((a * np.uint32(0x01010101)) >> 24).astype(np.int64)


_cache = {}


def idx_pc(n):
    if n not in _cache:
        idx = np.arange(1 << n, dtype=np.uint32)
        _cache[n] = (idx, popcount32(idx))
    return _cache[n]


def coords(n):
    """Matrix X of shape (2^n, n), X[x, i] = x_i in {+1,-1} (float64)."""
    idx, _ = idx_pc(n)
    X = np.empty((1 << n, n), dtype=np.float64)
    for i in range(n):
        X[:, i] = 1.0 - 2.0 * ((idx >> i) & 1)
    return X


def sgn(v):
    return np.where(v > 0, 1.0, -1.0)


def wht(f):
    """Normalised Walsh transform: returns c with c[S] = E f chi_S."""
    a = np.array(f, dtype=np.float64, copy=True)
    N = a.shape[0]
    h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        u = a[:, 0, :].copy()
        t = a[:, 1, :]
        a[:, 0, :] = u + t
        a[:, 1, :] = u - t
        a = a.reshape(N)
        h *= 2
    return a / N


def iwht(c):
    """Inverse of wht: returns the function sum_S c[S] chi_S."""
    return wht(c) * c.shape[0]


def HI(c, n):
    _, pc = idx_pc(n)
    c2 = c * c
    nz = c2 > 1e-300
    H = float(-(c2[nz] * np.log2(c2[nz])).sum())
    I = float((pc * c2).sum())
    return H, I


def influences(c, n):
    idx, _ = idx_pc(n)
    c2 = c * c
    return np.array([c2[((idx >> i) & 1).astype(bool)].sum() for i in range(n)])


# ----------------------------------------------------------------------------- rank quantities

def level_by_coord(c, n):
    """W[i, s] = sum over S containing i with |S| = s of fhat(S)^2."""
    idx, pc = idx_pc(n)
    c2 = c * c
    W = np.zeros((n, n + 1))
    for i in range(n):
        m = ((idx >> i) & 1).astype(bool)
        W[i] = np.bincount(pc[m], weights=c2[m], minlength=n + 1)
    return W


def rank_cost_matrix(c, n, units=None):
    """cost[u, t-1] = sum over coordinates i in unit u of sum_{S ni i} fhat(S)^2 ln+(t/|S|),
    t = 1..(number of units).  Sigma_r(f) = sum_u cost[u, rank(u)-1]."""
    W = level_by_coord(c, n)
    if units is None:
        units = np.arange(n)
    units = np.asarray(units)
    m = units.max() + 1
    s = np.arange(n + 1, dtype=np.float64)
    s[0] = 1.0
    t = np.arange(1, m + 1, dtype=np.float64)
    L = np.log(np.maximum(t[None, :] / s[:, None], 1.0))  # (n+1, m)
    L[0, :] = 0.0
    Ci = W @ L  # (n, m)
    cost = np.zeros((m, m))
    for i in range(n):
        cost[units[i]] += Ci[i]
    return cost


def sigma_of_order(c, n, unit_order, units=None):
    """Sigma for a given order of the units (unit_order[k] = unit placed at rank k+1)."""
    cost = rank_cost_matrix(c, n, units)
    rank = np.empty(len(unit_order), dtype=int)
    rank[np.asarray(unit_order)] = np.arange(len(unit_order))
    return float(sum(cost[u, rank[u]] for u in range(len(unit_order))))


def phi_min(c, n, units=None):
    """min over unit orders of Sigma_r(f), and an optimal order (exact, Hungarian method)."""
    cost = rank_cost_matrix(c, n, units)
    r, col = linear_sum_assignment(cost)
    val = float(cost[r, col].sum())
    order = np.empty(len(col), dtype=int)
    order[col] = r
    return val, order


def lemma3_Q(c, n, unit_order, units=None):
    """For each coordinate i with Inf_i > 0: Q_i = E_nu ln(N_i / (b(T)+1)), nu(T) = fhat(T+i)^2/Inf_i,
    N_i = rank of i's unit, b(T) = number of units strictly before i's unit that T meets.
    Returns array (nan where Inf_i = 0)."""
    idx, pc = idx_pc(n)
    c2 = c * c
    if units is None:
        units = np.arange(n)
    units = np.asarray(units)
    m = units.max() + 1
    rank = np.empty(m, dtype=int)
    rank[np.asarray(unit_order)] = np.arange(1, m + 1)
    unit_masks = np.zeros(m, dtype=np.uint64)
    for i in range(n):
        unit_masks[units[i]] |= np.uint64(1 << i)
    Q = np.full(n, np.nan)
    for i in range(n):
        m_i = ((idx >> i) & 1).astype(bool)
        inf = c2[m_i].sum()
        if inf < 1e-15:
            continue
        N = rank[units[i]]
        before = [u for u in range(m) if rank[u] < N]
        S = idx[m_i].astype(np.uint64)
        b = np.zeros(S.shape[0], dtype=np.int64)
        for u in before:
            b += ((S & unit_masks[u]) != 0)
        Q[i] = float((c2[m_i] * np.log(N / (b + 1.0))).sum() / inf)
    return Q


def partial_stab(c, n, i, noise_units_mask_list, eta):
    """sum_{S ni i} fhat(S)^2 (1-eta)^{b(S)} / Inf_i where b(S) = number of listed units met by S\\{i}."""
    idx, _ = idx_pc(n)
    c2 = c * c
    m_i = ((idx >> i) & 1).astype(bool)
    inf = c2[m_i].sum()
    S = idx[m_i].astype(np.uint64)
    b = np.zeros(S.shape[0], dtype=np.int64)
    for msk in noise_units_mask_list:
        b += ((S & np.uint64(msk)) != 0)
    return float((c2[m_i] * (1.0 - eta) ** b).sum() / inf)


def derivative_indicator(f, n, i):
    idx, _ = idx_pc(n)
    return (f != f[idx ^ np.uint32(1 << i)]).astype(np.float64)


def pointwise_exit(f, n, i, noise_units_mask_list, eta):
    """Exact function x -> Pr[D_i f(y) != 0 | x], y = x with each listed unit re-randomised
    independently with probability eta.  Computed as T h with h = 1[D_i f != 0]."""
    idx, _ = idx_pc(n)
    h = derivative_indicator(f, n, i)
    hc = wht(h)
    b = np.zeros(1 << n, dtype=np.int64)
    for msk in noise_units_mask_list:
        b += ((idx.astype(np.uint64) & np.uint64(msk)) != 0)
    return iwht(hc * (1.0 - eta) ** b), h


# ----------------------------------------------------------------------------- orders

def round_robin(orders):
    """Interleave k orders (lists of units) round robin; each round every order places its
    highest not-yet-placed unit."""
    placed = []
    seen = set()
    ptr = [0] * len(orders)
    total = len(set().union(*[set(o) for o in orders]))
    while len(placed) < total:
        for l, o in enumerate(orders):
            while ptr[l] < len(o) and o[ptr[l]] in seen:
                ptr[l] += 1
            if ptr[l] < len(o):
                u = o[ptr[l]]
                placed.append(u)
                seen.add(u)
    return placed


# ----------------------------------------------------------------------------- constants

def fei_constant(Lval, d=1):
    """C = 3 + min_{a>1} [1 + ln d + ln(a/(a-1)) + a Lval]/ln 2 (closed-form minimiser a(a-1) = 1/Lval)."""
    a = (1 + np.sqrt(1 + 4.0 / Lval)) / 2
    return 3 + (1 + np.log(d) + np.log(a / (a - 1)) + a * Lval) / np.log(2)


B_LTF = 3 * np.sqrt(3 / np.pi)
L1 = 2 * np.log(B_LTF) + 2
