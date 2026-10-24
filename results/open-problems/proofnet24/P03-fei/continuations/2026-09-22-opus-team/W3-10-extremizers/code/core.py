"""W3-10 core: exact spectral quantities, block (composition) structure, decomposition trees.

Conventions (as in CONTEXT.md): a Boolean function on n variables is an int8 truth table of length N = 2^n,
entry x in {+1,-1} (bit i of the index x is coordinate i; -1 means "true").  Integer Walsh transform
W[S] = sum_x f(x) (-1)^{|x&S|}; fhat(S) = W[S]/N.  Entropy in bits.

Per coordinate i (T ranges over sets not containing i): u_T = fhat(T), v_T = fhat(T+i).
  Inf_i  = sum v_T^2
  B_i    = sum E(u_T^2, v_T^2),  E(x,y) = phi(x)+phi(y)-phi(x+y),  phi(t) = t log2(1/t)
  Delta_i = H(f) - (H(f_+)+H(f_-))/2,   f_+- have coefficients u_T +- v_T
  rho_0(f) = min over relevant i of Delta_i/Inf_i.
"""
import os
import numpy as np
import numba as nb

LOG2 = np.log(2.0)


def polite():
    import psutil
    p = psutil.Process()
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])


@nb.njit(cache=True)
def phi(t):
    if t <= 0.0:
        return 0.0
    return -t * np.log(t) / 0.6931471805599453


@nb.njit(cache=True)
def walsh_int(tt):
    """Integer Walsh transform of a +-1 table (int64 output)."""
    N = tt.shape[0]
    a = np.empty(N, np.int64)
    for i in range(N):
        a[i] = tt[i]
    h = 1
    while h < N:
        for s in range(0, N, 2 * h):
            for j in range(s, s + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2
    return a


@nb.njit(cache=True)
def popc(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@nb.njit(cache=True)
def stats_from_walsh(W, n):
    """Returns (H, I, mean, Inf[n], Delta[n], B[n]) from the integer Walsh vector."""
    N = W.shape[0]
    inv = 1.0 / N
    H = 0.0
    I = 0.0
    for S in range(N):
        p = (W[S] * inv) ** 2
        H += phi(p)
        I += popc(S) * p
    Inf = np.zeros(n)
    Dl = np.zeros(n)
    Bv = np.zeros(n)
    for i in range(n):
        bit = 1 << i
        Hp = 0.0
        Hm = 0.0
        Bs = 0.0
        inf = 0.0
        for T in range(N):
            if T & bit:
                continue
            u = W[T] * inv
            v = W[T | bit] * inv
            a = u * u
            b = v * v
            inf += b
            Bs += phi(a) + phi(b) - phi(a + b)
            Hp += phi((u + v) ** 2)
            Hm += phi((u - v) ** 2)
        Inf[i] = inf
        Bv[i] = Bs
        Dl[i] = H - 0.5 * (Hp + Hm)
    return H, I, W[0] * inv, Inf, Dl, Bv


def stats(tt):
    tt = np.ascontiguousarray(tt, dtype=np.int8)
    n = int(round(np.log2(tt.shape[0])))
    W = walsh_int(tt)
    H, I, mu, Inf, Dl, B = stats_from_walsh(W, n)
    rel = Inf > 1e-15
    out = dict(n=n, H=H, I=I, mean=mu, Inf=Inf, Delta=Dl, B=B, nrel=int(rel.sum()))
    if rel.any():
        r = Dl[rel] / Inf[rel]
        out["rho0"] = float(r.min())
        out["rho_arg"] = int(np.nonzero(rel)[0][np.argmin(r)])
        out["minB"] = float((B[rel] / Inf[rel]).min())
        out["maxB"] = float((B[rel] / Inf[rel]).max())
    else:
        out["rho0"] = out["minB"] = out["maxB"] = float("nan")
        out["rho_arg"] = -1
    out["ratio"] = H / I if I > 0 else float("nan")
    out["J"] = H / (I - 1.0) if (abs(mu) < 1e-15 and I > 1 + 1e-12) else float("nan")
    return out


# ------------------------------------------------------------------ bits and tables
def bits_of(n):
    x = np.arange(1 << n)
    return ((x[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)


def tt_from_pred(n, pred):
    """pred(bits) -> bool 'true'; returns +-1 table with -1 = true."""
    b = bits_of(n)
    return np.array([-1 if pred(b[k]) else 1 for k in range(1 << n)], dtype=np.int8)


def relevant(tt):
    N = tt.shape[0]
    n = int(round(np.log2(N)))
    x = np.arange(N)
    return [i for i in range(n) if np.any(tt != tt[x ^ (1 << i)])]


def compress(tt):
    """Drop irrelevant variables; returns (table on the relevant variables, list of them)."""
    rel = relevant(tt)
    n = int(round(np.log2(tt.shape[0])))
    k = len(rel)
    y = np.arange(1 << k)
    x = np.zeros(1 << k, dtype=np.int64)
    for j, i in enumerate(rel):
        x |= ((y >> j) & 1) << i
    return tt[x].copy(), rel


def subfunction_index(n, A, B):
    """Index array idx[a, b] = x with x_A = bits(a), x_B = bits(b)."""
    a = np.arange(1 << len(A))
    b = np.arange(1 << len(B))
    X = np.zeros((a.size, b.size), dtype=np.int64)
    for j, i in enumerate(A):
        X |= (((a >> j) & 1) << i)[:, None]
    for j, i in enumerate(B):
        X |= (((b >> j) & 1) << i)[None, :]
    return X


def cofactor_classes(tt, A):
    """Distinct functions of x_B obtained by fixing x_A (B = complement); returns (labels over x_A, list of tables)."""
    n = int(round(np.log2(tt.shape[0])))
    B = [i for i in range(n) if i not in A]
    X = subfunction_index(n, A, B)
    rows = tt[X]
    keys = {}
    lab = np.empty(rows.shape[0], dtype=np.int64)
    tabs = []
    for r in range(rows.shape[0]):
        k = rows[r].tobytes()
        if k not in keys:
            keys[k] = len(tabs)
            tabs.append(rows[r].copy())
        lab[r] = keys[k]
    return lab, tabs


def find_blocks(tt, max_count=None):
    """All blocks A (2 <= |A| <= k-1 of the k relevant variables) with at most 2 distinct cofactors."""
    rel = relevant(tt)
    k = len(rel)
    out = []
    if k < 3:
        return out
    for mask in range(1, 1 << k):
        m = bin(mask).count("1")
        if m < 2 or m > k - 1:
            continue
        A = [rel[j] for j in range(k) if (mask >> j) & 1]
        lab, tabs = cofactor_classes(tt, A)
        if len(tabs) <= 2:
            out.append(tuple(A))
            if max_count and len(out) >= max_count:
                break
    return out


def is_prime(tt):
    return len(find_blocks(tt, max_count=1)) == 0 and len(relevant(tt)) >= 3


def decompose(tt, names=None):
    """Recursive disjoint-decomposition tree as a string.  Uses a maximal block at each step.
    Leaves: variable names; nodes: 'P<k>[hex](...)' for a prime k-input gate, or AND/OR/XOR/NOT forms."""
    tt = np.asarray(tt, dtype=np.int8)
    n = int(round(np.log2(tt.shape[0])))
    if names is None:
        names = ["x%d" % i for i in range(n)]
    ct, rel = compress(tt)
    nm = [names[i] for i in rel]
    k = len(rel)
    if k == 0:
        return "T" if ct[0] == -1 else "F"
    if k == 1:
        return nm[0] if ct[1] == -1 else "~" + nm[0]
    blocks = find_blocks(ct)
    if not blocks:
        return gate_name(ct, nm)
    # choose a maximal block (largest), ties by first
    A = max(blocks, key=len)
    lab, tabs = cofactor_classes(ct, list(A))
    # g(x_A) = label (0 -> first cofactor, 1 -> second)
    kA = len(A)
    g = np.where(lab == 0, 1, -1).astype(np.int8)  # g true (-1) when x_A gives cofactor #1
    Bv = [i for i in range(k) if i not in A]
    # outer G on (z, x_B): z = g value; G(z=+1,.) = tabs[0], G(z=-1,.) = tabs[1]
    kb = len(Bv)
    G = np.empty(1 << (kb + 1), dtype=np.int8)
    for zb in range(2):
        for b in range(1 << kb):
            G[zb | (b << 1)] = tabs[zb][b]
    sub = decompose(g, [nm[i] for i in A])
    outer = decompose(G, ["(" + sub + ")"] + [nm[i] for i in Bv])
    return outer


def gate_name(ct, nm):
    k = len(nm)
    w = walsh_int(ct)
    ntrue = int((ct == -1).sum())
    N = 1 << k
    if k == 2:
        if ntrue == 1:
            # AND with polarities: find the true point
            x = int(np.nonzero(ct == -1)[0][0])
            lits = [(nm[i] if (x >> i) & 1 else "~" + nm[i]) for i in range(2)]
            return "AND(" + ",".join(lits) + ")"
        if ntrue == 3:
            x = int(np.nonzero(ct == 1)[0][0])
            lits = [(("~" + nm[i]) if (x >> i) & 1 else nm[i]) for i in range(2)]
            return "OR(" + ",".join(lits) + ")"
        # XOR type
        return ("XOR(" if ct[0] == 1 else "XNOR(") + ",".join(nm) + ")"
    return "P%d[%s|%d/%d](%s)" % (k, ''.join('1' if v == -1 else '0' for v in ct), ntrue, N, ",".join(nm))


# ------------------------------------------------------------------ fast block search (numba)
@nb.njit(cache=True)
def _deposit(v, idx, cnt):
    x = 0
    for j in range(cnt):
        if (v >> j) & 1:
            x |= 1 << idx[j]
    return x


@nb.njit(cache=True)
def _is_block(tt, Aidx, nA, Bidx, nB):
    """True iff the cofactors over x_A (functions of x_B) take at most two distinct values."""
    NB = 1 << nB
    xb = np.empty(NB, np.int64)
    for b in range(NB):
        xb[b] = _deposit(b, Bidx, nB)
    r1 = -1
    r2 = -1
    for a in range(1 << nA):
        xa = _deposit(a, Aidx, nA)
        if r1 == -1:
            r1 = xa
            continue
        same1 = True
        for b in range(NB):
            if tt[xa | xb[b]] != tt[r1 | xb[b]]:
                same1 = False
                break
        if same1:
            continue
        if r2 == -1:
            r2 = xa
            continue
        same2 = True
        for b in range(NB):
            if tt[xa | xb[b]] != tt[r2 | xb[b]]:
                same2 = False
                break
        if not same2:
            return False
    return True


@nb.njit(cache=True)
def blocks_nb(tt, rel, first_only):
    k = rel.shape[0]
    out = []
    Aidx = np.empty(k, np.int64)
    Bidx = np.empty(k, np.int64)
    for m in range(1, 1 << k):
        sz = 0
        mm = m
        while mm:
            mm &= mm - 1
            sz += 1
        if sz < 2 or sz > k - 1:
            continue
        ca = 0
        cb = 0
        for j in range(k):
            if (m >> j) & 1:
                Aidx[ca] = rel[j]
                ca += 1
            else:
                Bidx[cb] = rel[j]
                cb += 1
        if _is_block(tt, Aidx, ca, Bidx, cb):
            out.append(m)
            if first_only:
                return out
    return out


def find_blocks_fast(tt, first_only=False):
    rel = np.array(relevant(tt), dtype=np.int64)
    if len(rel) < 3:
        return []
    ms = blocks_nb(np.ascontiguousarray(tt, dtype=np.int8), rel, first_only)
    return [tuple(int(rel[j]) for j in range(len(rel)) if (m >> j) & 1) for m in ms]


def is_prime_fast(tt):
    return len(relevant(tt)) >= 3 and len(find_blocks_fast(tt, first_only=True)) == 0


# route the public names to the numba implementation (validated against the slow version in logs/test_fast_blocks)
find_blocks_slow = find_blocks
is_prime_slow = is_prime


def find_blocks(tt, max_count=None):
    return find_blocks_fast(tt, first_only=(max_count == 1))


def is_prime(tt):
    return is_prime_fast(tt)
