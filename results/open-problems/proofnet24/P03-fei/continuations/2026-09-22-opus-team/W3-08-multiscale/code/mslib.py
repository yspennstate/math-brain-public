"""Multiscale (random block restriction) quantities for FEI.  W3-08, 23 September 2026.

Conventions (same as F4): a Boolean function on n variables is a +-1 truth table of length 2^n,
entry x (bit i of x = coordinate i; bit 0 means x_i = +1).  fhat(S) = 2^-n sum_x f(x) (-1)^{|x & S|}.
Entropies in bits.

For a set J of free coordinates and x in {-1,1}^{J^c}, f_{J,x} is the restriction of f that fixes the
coordinates outside J to x.  For every mask J the routine restr_profile returns
    EH[J] = E_x H(f_{J,x})                       (x uniform)
    HT[J] = H(S cap J)                           (entropy of the trace law A -> sum_{B in J^c} fhat(A u B)^2)
so that, with H = H(f),  M_J = HT[J] - EH[J]  (mixing information I(x;A))  and  L_J = H - HT[J]
(location entropy H(S minus J | S cap J)).

Exactness: after the partial Walsh transforms every coefficient is k / 2^{|J|} with an integer
|k| <= 2^{|J|}, so the transforms are exact in float64 and phi(c^2) = c^2 (2|J| - 2 log2|k|) is
evaluated from a table of log2 of integers.
"""
import numpy as np
import numba as nb


def polite():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        cpus = [c for c in (2, 3, 10, 11, 12, 13, 14, 15) if c < psutil.cpu_count()]
        p.cpu_affinity(cpus)
    except Exception as e:  # never fail on politeness
        print("[polite] could not set priority/affinity:", e)


@nb.njit(cache=True)
def _ctz(t):
    c = 0
    while (t & 1) == 0:
        t >>= 1
        c += 1
    return c


@nb.njit(cache=True)
def fwht(tt):
    """Normalised Walsh-Hadamard transform: returns fhat (float64)."""
    N = tt.shape[0]
    a = tt.astype(np.float64).copy()
    h = 1
    while h < N:
        for x in range(N):
            if (x & h) == 0:
                u = a[x]
                v = a[x | h]
                a[x] = u + v
                a[x | h] = u - v
        h <<= 1
    for x in range(N):
        a[x] /= N
    return a


@nb.njit(cache=True)
def entropy_bits(p):
    s = 0.0
    for q in p:
        if q > 0.0:
            s -= q * np.log2(q)
    return s


@nb.njit(cache=True)
def popcount(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@nb.njit(cache=True)
def influences(fh, n):
    N = fh.shape[0]
    inf = np.zeros(n)
    for S in range(N):
        w = fh[S] * fh[S]
        if w > 0.0:
            for i in range(n):
                if (S >> i) & 1:
                    inf[i] += w
    return inf


@nb.njit(cache=True)
def restr_profile(tt, n, need_trace):
    """Exact E_x H(f_{J,x}) and H(S cap J) for every mask J (Gray-code enumeration of J)."""
    N = 1 << n
    a = np.empty(N)
    for x in range(N):
        a[x] = float(tt[x])
    lg = np.zeros(N + 1)
    for k in range(1, N + 1):
        lg[k] = np.log2(k)
    EH = np.zeros(N)
    HT = np.zeros(N)
    tr = np.zeros(N)
    J = 0
    s = 0
    for t in range(1, N):
        i = _ctz(t)
        bit = 1 << i
        if (J & bit) == 0:
            for x in range(N):
                if (x & bit) == 0:
                    u = a[x]
                    v = a[x | bit]
                    a[x] = 0.5 * (u + v)
                    a[x | bit] = 0.5 * (u - v)
            J |= bit
            s += 1
        else:
            for x in range(N):
                if (x & bit) == 0:
                    u = a[x]
                    v = a[x | bit]
                    a[x] = u + v
                    a[x | bit] = u - v
            J &= ~bit
            s -= 1
        scale = float(1 << s)
        acc = 0.0
        for x in range(N):
            v = a[x]
            if v != 0.0:
                k = int(abs(v) * scale + 0.5)
                acc += v * v * (2.0 * s - 2.0 * lg[k])
        EH[J] = acc / float(1 << (n - s))
        if need_trace:
            for x in range(N):
                tr[x & J] += a[x] * a[x]
            ht = 0.0
            den = float(1 << (n - s))
            for x in range(N):
                if (x & J) == x:
                    q = tr[x] / den
                    if q > 0.0:
                        ht -= q * np.log2(q)
                    tr[x] = 0.0
            HT[J] = ht
    return EH, HT


@nb.njit(cache=True)
def restr_mean_hist(tt, n):
    """Counts of the restricted mean nu = E_y f(y,x) = k/2^s over all (J,x), |J| = s.

    Returns H[s, k + 2^n] (only |k| <= 2^s used).  Weight of (J,x) under the delta-random
    restriction: delta^s (1-delta)^(n-s) 2^-(n-s)."""
    N = 1 << n
    a = np.empty(N)
    for x in range(N):
        a[x] = float(tt[x])
    Hc = np.zeros((n + 1, 2 * N + 1))
    # J = empty: nu = f(x) = +-1
    for x in range(N):
        Hc[0, int(a[x]) + N] += 1.0
    J = 0
    s = 0
    for t in range(1, N):
        i = _ctz(t)
        bit = 1 << i
        if (J & bit) == 0:
            for x in range(N):
                if (x & bit) == 0:
                    u = a[x]
                    v = a[x | bit]
                    a[x] = 0.5 * (u + v)
                    a[x | bit] = 0.5 * (u - v)
            J |= bit
            s += 1
        else:
            for x in range(N):
                if (x & bit) == 0:
                    u = a[x]
                    v = a[x | bit]
                    a[x] = u + v
                    a[x | bit] = u - v
            J &= ~bit
            s -= 1
        scale = float(1 << s)
        for x in range(N):
            if (x & J) == 0:
                k = int(np.round(a[x] * scale))
                Hc[s, k + N] += 1.0
    return Hc


def size_weights(n, delta):
    s = np.arange(n + 1)
    return delta ** s * (1.0 - delta) ** (n - s)


def per_size_sums(vals, n):
    """sum of vals[J] over |J| = s, s = 0..n."""
    N = 1 << n
    pc = np.array([bin(J).count("1") for J in range(N)])
    return np.bincount(pc, weights=vals, minlength=n + 1)


def basic(tt, n):
    fh = fwht(np.asarray(tt, dtype=np.int64))
    p = fh * fh
    H = entropy_bits(p)
    inf = influences(fh, n)
    return fh, p, H, inf


def multiscale_summary(tt, n, deltas=(0.25, 0.5, 0.75, 0.9), need_trace=True):
    """kappa_delta = (H - E H(f_{J,x})) / ((1-delta) I), and the mixing/location split."""
    tt = np.asarray(tt, dtype=np.int64)
    fh, p, H, inf = basic(tt, n)
    I = inf.sum()
    EH, HT = restr_profile(tt, n, need_trace)
    cEH = per_size_sums(EH, n)
    cHT = per_size_sums(HT, n)
    out = {"n": n, "H": H, "I": I, "H/I": H / I if I > 0 else 0.0}
    for d in deltas:
        w = size_weights(n, d)
        EHd = float((w * cEH).sum())
        HTd = float((w * cHT).sum())
        D = H - EHd
        out[f"kappa_{d}"] = D / ((1 - d) * I) if I > 0 else 0.0
        if need_trace:
            out[f"M_{d}"] = (HTd - EHd) / ((1 - d) * I) if I > 0 else 0.0
            out[f"L_{d}"] = (H - HTd) / ((1 - d) * I) if I > 0 else 0.0
    # single-coordinate quantities from the profile: J = all but i
    full = (1 << n) - 1
    rel = [i for i in range(n) if inf[i] > 1e-15]
    drops = np.array([H - EH[full & ~(1 << i)] for i in range(n)])
    if rel:
        out["rho0"] = min(drops[i] / inf[i] for i in rel)
        out["avgcoord"] = drops.sum() / I
    return out, EH, HT, inf, H, I
