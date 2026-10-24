"""Core library for group W2-C (reference measures for FEI), 23 September 2026.

Conventions (same as CONTEXT.md): a Boolean function on n variables is a +-1 truth table of length 2^n,
entry x (bit i of x = coordinate i), -1 = "true". fhat(S) = 2^-n sum_x f(x) (-1)^{|x & S|}.
The spectral sample S has law p[S] = fhat(S)^2 (S encoded as a bitmask). Entropies in bits.

Reference-measure costs computed here (all are expected code lengths E_S log2(1/Q(S)) >= H(f)):
  * tree_dp       : optimal binary tree-Markov (hierarchical) reference, exact subset DP, O(3^n).
  * tree_cost     : tree-Markov reference for a given binary tree.
  * levelwise     : optimal level-wise product (conditional Bernoulli) reference = H(|S|) + sum_k P_k Hmax_k.
  * f5_rank_cost  : exact cost of F5's rank-weighted reference (Lemma 6) for a given ordering and exponent a.
"""
import math
import numpy as np
import numba as nb

LOG2 = math.log(2.0)


def set_polite():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 14, 15])
    except Exception as e:  # never fail on politeness
        print("[polite] could not set priority/affinity:", e)


# ----------------------------------------------------------------------------- spectra
def wht(tt):
    a = np.array(tt, dtype=np.float64, copy=True)
    N = a.shape[-1]
    h = 1
    shp = a.shape[:-1]
    while h < N:
        a = a.reshape(shp + (N // (2 * h), 2, h))
        x = a[..., 0, :].copy()
        y = a[..., 1, :]
        a[..., 0, :] = x + y
        a[..., 1, :] = x - y
        a = a.reshape(shp + (N,))
        h *= 2
    return a / N


def popcounts(N):
    x = np.arange(N, dtype=np.int64)
    c = np.zeros(N, dtype=np.int64)
    while x.any():
        c += x & 1
        x >>= 1
    return c


def phi_np(p):
    p = np.asarray(p, dtype=np.float64)
    out = np.zeros_like(p)
    m = p > 0
    out[m] = -p[m] * np.log2(p[m])
    return out


def h2(q):
    return float(phi_np(np.array([q, 1.0 - q])).sum())


def spectrum(tt):
    fh = wht(tt)
    return fh * fh


def H_of(p):
    return float(phi_np(p).sum())


def I_of(p, n):
    return float((p * popcounts(1 << n)).sum())


def influences(p, n):
    N = 1 << n
    S = np.arange(N)
    return np.array([p[((S >> i) & 1) == 1].sum() for i in range(n)])


def level_dist(p, n):
    pc = popcounts(1 << n)
    return np.bincount(pc, weights=p, minlength=n + 1)


def zeta_subset(p, n):
    """g[A] = sum_{T subset of A} p[T]."""
    g = np.array(p, dtype=np.float64, copy=True)
    N = 1 << n
    for i in range(n):
        g = g.reshape(N // (2 << i), 2, 1 << i)
        g[:, 1, :] += g[:, 0, :]
        g = g.reshape(N)
    return g


def empty_prob(p, n):
    """z[B] = Pr[S cap B = empty] = sum_{T subset of complement(B)} p[T]."""
    g = zeta_subset(p, n)
    N = 1 << n
    idx = (N - 1) ^ np.arange(N)
    return g[idx]


# ----------------------------------------------------------------------------- tree-Markov references
@nb.njit(cache=True)
def _phi(x):
    if x <= 0.0:
        return 0.0
    return -x * math.log(x) / 0.6931471805599453


@nb.njit(cache=True)
def _node_cost(z1, z2, z12):
    pL = z2 - z12
    pR = z1 - z12
    pLR = 1.0 - z1 - z2 + z12
    hit = 1.0 - z12
    if pL < 0.0:
        pL = 0.0
    if pR < 0.0:
        pR = 0.0
    if pLR < 0.0:
        pLR = 0.0
    if hit < 0.0:
        hit = 0.0
    return _phi(pL) + _phi(pR) + _phi(pLR) - _phi(hit)


@nb.njit(cache=True)
def tree_dp(z, n):
    """best[B] = min over binary trees on the coordinate set B of sum over internal nodes of
    Pr[node hit] * H(hit-pattern of its two children | node hit).  arg[B] = left child mask."""
    N = 1 << n
    best = np.zeros(N)
    arg = np.zeros(N, dtype=np.int64)
    for B in range(1, N):
        if (B & (B - 1)) == 0:
            continue
        low = B & (-B)
        rest = B ^ low
        zB = z[B]
        bv = 1e300
        ba = 0
        s = rest
        while True:
            B1 = low | s
            B2 = B ^ B1
            if B2 != 0:
                c = _node_cost(z[B1], z[B2], zB) + best[B1] + best[B2]
                if c < bv:
                    bv = c
                    ba = B1
            if s == 0:
                break
            s = (s - 1) & rest
        best[B] = bv
        arg[B] = ba
    return best, arg


def tree_from_arg(arg, B):
    if B & (B - 1) == 0:
        return int(B).bit_length() - 1
    L = int(arg[B])
    return (tree_from_arg(arg, L), tree_from_arg(arg, B ^ L))


def tree_mask(t):
    if isinstance(t, (int, np.integer)):
        return 1 << int(t)
    m = 0
    for c in t:
        m |= tree_mask(c)
    return m


def tree_cost(z, t):
    """sum of node costs of a binary (or general) tree t given empty-probabilities z.
    For a node with children c_1..c_m (m >= 2) the pattern law is computed by inclusion-exclusion
    over the children masks (only practical for small m)."""
    if isinstance(t, (int, np.integer)):
        return 0.0
    kids = [tree_mask(c) for c in t]
    B = 0
    for k in kids:
        B |= k
    m = len(kids)
    # Pr[exactly the children in pattern A are hit] = sum_{C superset A} (-1)^{|C|-|A|} ... use empties:
    # Pr[children outside A empty and all in A hit] = sum_{D subset A} (-1)^{|D|} z[(union of kids not in A) | union kids in D]
    cost = 0.0
    hit = 1.0 - z[B]
    for A in range(1, 1 << m):
        out = 0
        for j in range(m):
            if not (A >> j) & 1:
                out |= kids[j]
        pr = 0.0
        Aj = [j for j in range(m) if (A >> j) & 1]
        for D in range(1 << len(Aj)):
            msk = out
            sgn = 1.0
            for t_ in range(len(Aj)):
                if (D >> t_) & 1:
                    msk |= kids[Aj[t_]]
                    sgn = -sgn
            pr += sgn * z[msk]
        if pr > 0:
            cost += -pr * math.log2(pr)
    cost -= (-hit * math.log2(hit)) if hit > 0 else 0.0
    return cost + sum(tree_cost(z, c) for c in t)


def tree_markov_H(p, n, t=None):
    """Expected code length of the tree-Markov reference (root bit + node costs). t=None -> optimal binary tree."""
    z = empty_prob(p, n)
    root = h2(float(p[0]))
    if t is None:
        best, arg = tree_dp(z, n)
        return root + float(best[(1 << n) - 1]), tree_from_arg(arg, (1 << n) - 1)
    return root + tree_cost(z, t), t


# ----------------------------------------------------------------------------- level-wise product references
def _esp_log(logw, k):
    """log e_j(w) for j = 0..k, stable (w = exp(logw))."""
    n = len(logw)
    E = np.full(k + 1, -np.inf)
    E[0] = 0.0
    for i in range(n):
        lw = logw[i]
        up = np.minimum(np.arange(i + 1, 0, -1)[:], k) if False else None
        # E_new[j] = logaddexp(E[j], E[j-1] + lw)
        E[1:] = np.logaddexp(E[1:], E[:-1] + lw)
    return E


def _cb_logZ_and_incl(logw, k):
    """log e_k(w) and inclusion probabilities of the conditional Bernoulli design of size k."""
    n = len(logw)
    # forward prefix: F[i][j] = log e_j(w_0..w_{i-1})
    F = np.full((n + 1, k + 1), -np.inf)
    F[0, 0] = 0.0
    for i in range(n):
        F[i + 1] = F[i]
        F[i + 1, 1:] = np.logaddexp(F[i, 1:], F[i, :-1] + logw[i])
    Bk = np.full((n + 2, k + 1), -np.inf)
    Bk[n, 0] = 0.0
    for i in range(n - 1, -1, -1):
        Bk[i] = Bk[i + 1]
        Bk[i, 1:] = np.logaddexp(Bk[i + 1, 1:], Bk[i + 1, :-1] + logw[i])
    logZ = F[n, k]
    incl = np.zeros(n)
    for i in range(n):
        # e_{k-1}(w without i) = sum_j e_j(prefix<i) e_{k-1-j}(suffix>i)
        a = F[i, :k]
        b = Bk[i + 1, :k][::-1]
        v = np.logaddexp.reduce(a + b)
        incl[i] = math.exp(logw[i] + v - logZ)
    return logZ, incl


def cb_maxent(m, k, iters=200, tol=1e-12):
    """Max entropy (nats) of a distribution on k-subsets with inclusion probabilities m (sum m = k).
    Coordinates with m=0 are dropped and m=1 are forced. Returns entropy in nats."""
    m = np.asarray(m, dtype=np.float64)
    keep = (m > 1e-15) & (m < 1 - 1e-12)
    forced = int(np.sum(m >= 1 - 1e-12))
    kk = k - forced
    mm = m[keep]
    if kk <= 0 or len(mm) == 0:
        return 0.0
    if kk >= len(mm):
        return 0.0
    # Newton-like fixed point on logw: logw += log(m/incl) (iterative proportional fitting for CP designs)
    logw = np.log(mm) - np.log1p(-mm)
    for it in range(iters):
        logZ, incl = _cb_logZ_and_incl(logw, kk)
        err = np.max(np.abs(incl - mm))
        if err < tol:
            break
        logw = logw + (np.log(mm) - np.log(np.maximum(incl, 1e-300))) * 1.0
        logw -= logw.mean()
    logZ, incl = _cb_logZ_and_incl(logw, kk)
    # entropy = E[log 1/pi(S)] under the maxent design with marginals mm = logZ - sum mm*logw
    return float(logZ - np.dot(incl, logw))


def levelwise_product_cost(p, n):
    """H(|S|) + sum_k P_k * Hmax(k-subsets | marginals of S given |S|=k), in bits.
    This is the smallest cost of any reference of the form Q(S) = rho(|S|) prod_{i in S} w_{|S|,i} / e_{|S|}(w_{|S|})."""
    N = 1 << n
    pc = popcounts(N)
    Pk = np.bincount(pc, weights=p, minlength=n + 1)
    cost = H_of(Pk)
    S = np.arange(N)
    bits = ((S[:, None] >> np.arange(n)[None, :]) & 1).astype(np.float64)
    for k in range(1, n + 1):
        if Pk[k] <= 1e-300:
            continue
        sel = pc == k
        m = (p[sel][:, None] * bits[sel]).sum(axis=0) / Pk[k]
        cost += Pk[k] * cb_maxent(m, k) / LOG2
    return cost


def f5_rank_cost(p, n, order, a):
    """Exact cost (bits) of F5's rank-weighted reference: H(|S|) + sum_k P_k E[log e_k(q_k) - sum_{i in S} log q_k(r(i)) | |S|=k],
    q_k(s) = min(1, (k/s)^a); order[r-1] = coordinate of rank r."""
    N = 1 << n
    pc = popcounts(N)
    Pk = np.bincount(pc, weights=p, minlength=n + 1)
    cost = H_of(Pk)
    rank = np.empty(n, dtype=np.int64)
    for r, c in enumerate(order):
        rank[c] = r + 1
    S = np.arange(N)
    bits = ((S[:, None] >> np.arange(n)[None, :]) & 1).astype(np.float64)
    for k in range(1, n + 1):
        if Pk[k] <= 1e-300:
            continue
        sel = pc == k
        m = (p[sel][:, None] * bits[sel]).sum(axis=0) / Pk[k]
        lq = np.minimum(0.0, a * (np.log(k) - np.log(rank.astype(np.float64))))
        E = _esp_log(lq, k)
        cost += Pk[k] * (E[k] - np.dot(m, lq)) / LOG2
    return cost


# ----------------------------------------------------------------------------- families
def tt_from_bits(n, fn):
    N = 1 << n
    x = np.arange(N)
    bits = ((x[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int64)
    v = fn(bits)
    return np.where(v, -1, 1).astype(np.int8)


def fam_majority(n):
    return tt_from_bits(n, lambda b: b.sum(1) * 2 > n)


def fam_and(n):
    return tt_from_bits(n, lambda b: b.sum(1) == n)


def fam_tribes(w, s):
    return tt_from_bits(w * s, lambda b: np.any(b.reshape(-1, s, w).all(2), axis=1))


def fam_bent(m2):
    return tt_from_bits(2 * m2, lambda b: (np.sum(b[:, :m2] * b[:, m2:], axis=1) & 1) == 1)


def fam_bent_flip(m2):
    """bent IP on 2*m2 variables plus z (last); z=1 flips the point y = all-ones."""
    n = 2 * m2 + 1

    def fn(b):
        y = b[:, :2 * m2]
        v = (np.sum(y[:, :m2] * y[:, m2:], axis=1) & 1) == 1
        flip = (b[:, 2 * m2] == 1) & (y.sum(1) == 2 * m2)
        return v ^ flip
    return tt_from_bits(n, fn)


def fam_recmaj(depth, perm=None):
    n = 3 ** depth

    def fn(b):
        v = b if perm is None else b[:, perm]
        while v.shape[1] > 1:
            v = (v.reshape(v.shape[0], -1, 3).sum(2) >= 2).astype(np.int64)
        return v[:, 0] == 1
    return tt_from_bits(n, fn)


def fam_addressing(k):
    n = k + (1 << k)

    def fn(b):
        a = np.zeros(b.shape[0], dtype=np.int64)
        for j in range(k):
            a |= b[:, j] << j
        return b[np.arange(b.shape[0]), k + a] == 1
    return tt_from_bits(n, fn)


def fam_mux(t0, t1, n):
    """x_0 selects: f(x0, y) = t0[y] if x0 = 0 else t1[y]; t0, t1 on n variables; result on n+1 variables (x0 = coordinate 0)."""
    N = 1 << (n + 1)
    x = np.arange(N)
    y = x >> 1
    sel = x & 1
    return np.where(sel == 0, t0[y], t1[y]).astype(np.int8)


def fam_maj_flip(n):
    """Maj_n(y) OR (z AND y = y*), y* a maximal false point; z = coordinate n. (F4 Prop 6.1)"""
    ystar = np.zeros(n, dtype=np.int64)
    ystar[:(n - 1) // 2] = 1

    def fn(b):
        y = b[:, :n]
        return (y.sum(1) * 2 > n) | ((b[:, n] == 1) & np.all(y == ystar[None, :], axis=1))
    return tt_from_bits(n + 1, fn)


def fam_ltf(w, theta):
    n = len(w)
    w = np.asarray(w, dtype=np.float64)
    return tt_from_bits(n, lambda b: (2 * b - 1) @ w - theta > 0)


def fam_chain(ops):
    """AND/OR chain x_0 op_0 (x_1 op_1 (x_2 ... x_{n-1})) with ops in {'&','|'}; n = len(ops)+1."""
    n = len(ops) + 1

    def fn(b):
        v = b[:, n - 1] == 1
        for j in range(n - 2, -1, -1):
            if ops[j] == '&':
                v = (b[:, j] == 1) & v
            else:
                v = (b[:, j] == 1) | v
        return v
    return tt_from_bits(n, fn)


def load_numaro():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    return np.load(os.path.join(here, "..", "..", "inputs", "numaro18_pm1_table.npy"))
