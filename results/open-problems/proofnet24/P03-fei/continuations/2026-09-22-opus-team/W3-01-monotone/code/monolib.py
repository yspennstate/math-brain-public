"""Core routines for the W3-01 monotone group.

Conventions (as in CONTEXT.md): a Boolean function is a truth table tt on n <= 6 variables stored as an
integer bitmask, bit x of tt = f(x) in {0,1} with 1 = true; bit i of x is the value of coordinate i.
The +-1 version is F(x) = (-1)^f(x) (true -> -1), Fhat(S) = 2^-n sum_x F(x) (-1)^{|S cap x|}.
For monotone f, Fhat({i}) = Inf_i >= 0.

H = sum Fhat^2 log2(1/Fhat^2), I = sum |S| Fhat^2.

Desirability (Isbell): j >= i ("j is at least as desirable as i") iff f(x^{j<-1,i<-0}) >= f(x^{j<-0,i<-1})
for every assignment of the other coordinates.  D(i) = {j : j >= i} (contains i).
"""
import numpy as np
import numba as nb

LN2 = np.log(2.0)


def setup_process():
    import psutil
    p = psutil.Process()
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    try:
        p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
    except Exception:
        pass


# ----------------------------------------------------------------------------------------------
# enumeration of monotone functions (Dedekind), n <= 6, as uint64 bitmasks
# ----------------------------------------------------------------------------------------------

def monotone_tables(n):
    """All monotone f on n variables as a sorted np.uint64 array (bit x = f(x))."""
    cur = np.array([0, 1], dtype=np.uint64)          # n = 0
    for m in range(1, n + 1):
        half = 1 << (m - 1)                            # table length of the (m-1)-variable pieces
        out = []
        for a in cur:
            # f0 = a (x_{m-1} = 0), f1 = b (x_{m-1} = 1), need a <= b bitwise
            ok = cur[(cur & a) == a]
            out.append(a | (ok << np.uint64(half)))
        cur = np.sort(np.concatenate(out))
    return cur


# ----------------------------------------------------------------------------------------------
# Walsh transform and basic quantities
# ----------------------------------------------------------------------------------------------

@nb.njit(cache=True)
def wht_int(tt, n):
    """Integer Walsh coefficients W[S] = sum_x F(x)(-1)^{|S cap x|} = 2^n Fhat(S)."""
    N = 1 << n
    w = np.empty(N, dtype=np.int64)
    for x in range(N):
        w[x] = -1 if (tt >> np.uint64(x)) & np.uint64(1) else 1
    h = 1
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                a = w[j]
                b = w[j + h]
                w[j] = a + b
                w[j + h] = a - b
        h *= 2
    return w


@nb.njit(cache=True)
def popcount(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@nb.njit(cache=True)
def entropy_influence(W, n):
    N = 1 << n
    scale = 1.0 / (N * N)
    H = 0.0
    I = 0.0
    for S in range(N):
        if W[S] != 0:
            p = W[S] * W[S] * scale
            H -= p * np.log2(p)
            I += popcount(S) * p
    return H, I


@nb.njit(cache=True)
def influences_from_W(W, n):
    N = 1 << n
    scale = 1.0 / (N * N)
    inf = np.zeros(n)
    for S in range(N):
        if W[S] != 0:
            p = W[S] * W[S] * scale
            for i in range(n):
                if (S >> i) & 1:
                    inf[i] += p
    return inf


@nb.njit(cache=True)
def desirability(tt, n):
    """dom[i, j] = True iff j >= i (j at least as desirable as i). dom[i,i] = True."""
    N = 1 << n
    dom = np.zeros((n, n), dtype=np.bool_)
    for i in range(n):
        dom[i, i] = True
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ok = True
            bi = 1 << i
            bj = 1 << j
            for x in range(N):
                if (x & bi) == 0 and (x & bj) != 0:
                    y = x ^ (bi | bj)        # x_j <- 0, x_i <- 1
                    fx = (tt >> np.uint64(x)) & np.uint64(1)
                    fy = (tt >> np.uint64(y)) & np.uint64(1)
                    if fx < fy:
                        ok = False
                        break
            dom[i, j] = ok
    return dom


@nb.njit(cache=True)
def relevant_mask(tt, n):
    N = 1 << n
    m = 0
    for i in range(n):
        bi = 1 << i
        for x in range(N):
            if (x & bi) == 0:
                if ((tt >> np.uint64(x)) & np.uint64(1)) != ((tt >> np.uint64(x | bi)) & np.uint64(1)):
                    m |= bi
                    break
    return m


@nb.njit(cache=True)
def width_and_profile(dom, rel, n):
    """Width of the desirability preorder restricted to relevant coordinates (max antichain, where
    i, j are comparable if dom[i,j] or dom[j,i]) and the dominance profile
    K = max_d #{j relevant : |D(j)| <= d} / d, with D(j) computed inside the relevant coordinates."""
    best = 0
    for A in range(1 << n):
        if (A & ~rel) != 0:
            continue
        ok = True
        c = 0
        for i in range(n):
            if (A >> i) & 1:
                c += 1
                for j in range(i + 1, n):
                    if (A >> j) & 1:
                        if dom[i, j] or dom[j, i]:
                            ok = False
                            break
                if not ok:
                    break
        if ok and c > best:
            best = c
    # profile
    dsz = np.zeros(n, dtype=np.int64)
    for i in range(n):
        if (rel >> i) & 1:
            c = 0
            for j in range(n):
                if (rel >> j) & 1 and dom[i, j]:
                    c += 1
            dsz[i] = c
    K = 0.0
    for d in range(1, n + 1):
        cnt = 0
        for i in range(n):
            if (rel >> i) & 1 and dsz[i] <= d:
                cnt += 1
        if cnt / d > K:
            K = cnt / d
    return best, K, dsz


# ----------------------------------------------------------------------------------------------
# rank-localisation quantities (F5 notation)
# ----------------------------------------------------------------------------------------------

@nb.njit(cache=True)
def lemma3_values(W, n, Umask):
    """For each i: sum_{T not ni i} Fhat(T+i)^2 ln(N_i/(|T cap U_i|+1)) / Inf_i, with N_i = |U_i|+1.
    Umask[i] = bitmask of U_i (must not contain i)."""
    N = 1 << n
    scale = 1.0 / (N * N)
    out = np.zeros(n)
    inf = np.zeros(n)
    for S in range(N):
        if W[S] == 0:
            continue
        p = W[S] * W[S] * scale
        for i in range(n):
            if (S >> i) & 1:
                U = Umask[i]
                Ni = popcount(U) + 1
                k = popcount(S & U)
                out[i] += p * np.log(Ni / (k + 1.0))
                inf[i] += p
    for i in range(n):
        if inf[i] > 0:
            out[i] /= inf[i]
    return out, inf


@nb.njit(cache=True)
def sigma_rank(W, n, rank):
    """Sigma_r(f) = E_S sum_{i in S} ln+(r(i)/|S|), rank[i] in 1..n."""
    N = 1 << n
    scale = 1.0 / (N * N)
    s = 0.0
    for S in range(N):
        if W[S] == 0 or S == 0:
            continue
        p = W[S] * W[S] * scale
        m = popcount(S)
        for i in range(n):
            if (S >> i) & 1:
                v = rank[i] / m
                if v > 1.0:
                    s += p * np.log(v)
    return s


# ----------------------------------------------------------------------------------------------
# generic (large n) truth tables as numpy arrays of +-1
# ----------------------------------------------------------------------------------------------

def fwht_float(F):
    """Normalised Walsh transform of a +-1 (or real) vector of length 2^n; returns Fhat."""
    a = np.array(F, dtype=np.float64).copy()
    N = a.size
    h = 1
    while h < N:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(N)
        h *= 2
    return a / N


def HI_from_hat(c, n):
    p = c * c
    nz = p > 0
    H = float(-(p[nz] * np.log2(p[nz])).sum())
    pc = np.array([bin(s).count("1") for s in range(1 << n)]) if n <= 16 else None
    if pc is None:
        pc = popcounts(n)
    I = float((pc * p).sum())
    return H, I


def popcounts(n):
    N = 1 << n
    pc = np.zeros(N, dtype=np.int64)
    for i in range(n):
        pc += (np.arange(N) >> i) & 1
    return pc


def desirability_array(f01, n):
    """f01: uint8 array of length 2^n (1 = true). dom[i,j] = j >= i."""
    N = 1 << n
    xs = np.arange(N)
    dom = np.eye(n, dtype=bool)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            sel = ((xs >> i) & 1 == 0) & ((xs >> j) & 1 == 1)
            x = xs[sel]
            y = x ^ ((1 << i) | (1 << j))
            dom[i, j] = bool(np.all(f01[x] >= f01[y]))
    return dom
